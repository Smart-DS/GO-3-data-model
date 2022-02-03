import abc
import argparse
import logging
from pathlib import Path
import re

from datamodel import datamodel_path, input_path

logger = logging.getLogger(__name__)


# After objects have been created, these files say how to assemble them
models = {
    "Input Data File": [
        "static_json",
        "time_series",
        # ("main", "Contingencies"), # contingencies are currently in the main 
        # file and poorly defined from a parsing perspective
        "parsing_mapping"
    ],
    "Output Data File": [
        "solution",
        "parsing_mapping"
    ]
}


class FileParser(abc.ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    @abc.abstractmethod
    def append(self, datamodel):
        pass


def create_objects(format_docs_dir):
    input_objects = {
        "static": {},
        "timeseries": {}
    }
    output_objects = {
        "static": {},
        "timeseries": {}
    }
    with open(format_docs_dir / "main.tex", encoding="utf8") as f:
        main_file = f.read()

    sections = _split(main_file, r"^\\section\{(.+)\}\s*$")
    object_section = "Naming Conventions"
    if not object_section in sections:
        section_names = "  \n".join([key for key in sections])
        raise ValueError(f"Did not find '{object_section}' in main.tex. Found:\n  {section_names}")
    section = sections["Naming Conventions"]

    candidates = _split(section, r"^\\subsection\{(.+)\}\s*$")

    for candidate, text in candidates.items():
        candidate = candidate.replace(" ","")
        tmp = _split(text, r"^\\paragraph\{(.+)\}.*$")
        if "Input Attributes" in tmp:
            logger.info(f"Processing {candidate} input attributes")
            # process input attribute table
            static_obj, timeseries_obj = get_objects_from_table(candidate, tmp["Input Attributes"])
            if (static_obj is None) and (timeseries_obj is None):
                logger.info(f"Unable to extract input attributes for {candidate}")
            else:
                if static_obj:
                    input_objects["static"][candidate] = static_obj
                if timeseries_obj:
                    input_objects["timeseries"][candidate] = timeseries_obj
        else:
            logger.info(f"No input attributes for {candidate}")
        
        if "Output Attributes" in tmp:
            logger.info(f"Processing {candidate} output attributes")
            # process output attribute table
            static_obj, timeseries_obj = get_objects_from_table(candidate, tmp["Output Attributes"])
            if (static_obj is None) and (timeseries_obj is None):
                logger.info(f"Unable to extract output attributes for {candidate}")
            else:
                if static_obj:
                    output_objects["static"][candidate] = static_obj
                if timeseries_obj:
                    output_objects["timeseries"][candidate] = timeseries_obj
        else:
            logger.info(f"No output attributes for {candidate}")

    return input_objects, output_objects


def get_objects_from_table(object_name, astr):
    static_result = f"class {object_name}(BidDSJsonBaseModel):\n"
    timeseries_result = f"class {object_name}(BidDSJsonBaseModel):\n"
    has_static = False; has_timeseries = False

    table_started = False; expect_meta = True
    for ln in astr.split("\n"):
        if not table_started:
            if ln.startswith("\\begin{tabular}"):
                table_started = True
            continue
        if ln.startswith("\\end{tabular}"):
            break
        if ln.strip().startswith("%"): # comment character
            continue
        if ln.strip() == "\\hline":
            expect_meta = True
            continue
        if ln.strip().startswith("{\\tt"):
            sec, field = parse_field(ln)
            if field:
                if sec == "S":
                    static_result += field
                    has_static = True
                elif sec == "T":
                    timeseries_result += field
                    has_timeseries = True
                else:
                    assert sec == "B", repr(sec)
                    static_result += field
                    timeseries_result += field
        elif expect_meta:
            meta = ln.split("&")[0].strip()
            static_result += f"\n    # {meta}\n"
            timeseries_result += f"\n    # {meta}\n"
            continue

    if not has_static:
        static_result = None
    if not has_timeseries:
        timeseries_result = None

    return (static_result, timeseries_result) if table_started else (None, None)


types_map = {
    "uid": "str",
    "uids": "List[str]",
    "String": "str",
    "Int": "int",
    "Float": "float",
    "\\$/p.u.": "float",
    "Float, p.u": "float",
    "Float, p.u.": "float",
    "Float, p.u./hr": "float",
    "Float, \\$/p.u.": "float",
    "Float, radian": "float",
    "Float, hr": "float",
    "p.u.": "float",
    "bool: true/false": "bool"
}

def parse_field(ln):
    name, desc, req, sec, sym = ln.split("&")
    sec = sec.strip()
    
    # get name
    m = re.match("\{\\\\tt\S* (.+)\}", name.strip())
    if not m:
        logger.warning(f"Unable to extract name from {name!r}")
        return sec, ""
    name = m.group(1).replace("\\_", "_")

    # get description and type
    m = re.match("(.*)\((.*)\)", desc.strip())
    if not m:
        logger.warning(f"Unable to partition {desc!r} into description and type")
        return sec, ""
    desc = m.group(1); type = m.group(2)

    choices = None
    if type in types_map:
        type = types_map[type]
    else:
        if type.startswith("String:"):
            # choices list
            choices = type.split(":")[1].strip().split(",")
            choices = [choice.strip().replace("\\_","_") for choice in choices]
            # TODO: Consider turning choices into an Enum and then setting type 
            # to be that Enum
            type = "String"
        elif type.startswith("Binary:"):
            choices = [0,1]
            type = "int"
        else:
            logger.warning(f"Unable to extract type from {type!r}")
            return sec, ""
    
    if req.lower().strip() == "n":
        type = f"Optional[{type}]"

    sep = "," if choices else ""
    
    result = f"""
    {name}: {type} = Field(
        title = "{name}",
        description = "{desc}"{sep}"""
   
    if choices:
        choices_str = str([choice for choice in choices]).replace("'", '"')
        result+= f"""
        options = {choices_str}"""
    
    result += """
    )\n"""
    return sec, result

    
def _split(astr, fmt):
    result = {}
    cur_name = None; cur_lines = []
    for ln in astr.split("\n"):
        m = re.match(fmt,ln)
        if m:
            if cur_name:
                result[cur_name] = "\n".join(cur_lines)
            cur_name = m.group(1)
            cur_lines = []
            continue
        if cur_name:
            cur_lines.append(ln)
    if cur_name:
        result[cur_name] = "\n".join(cur_lines)
    return result


def create_models(format_docs_dir, input_objects, output_objects):
    for model_name, files in models.items():
        datamodel = """
import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union

from .base import BidDSJsonBaseModel\n
        """

        for file in files:
            pass
            # file_parser = FileParser(format_docs_dir / f"{file}.tex")
            # file_parser.append(datamodel)

        with open(datamodel_path / (model_name.replace(" ","_").lower() + ".py"), "w") as f:
            f.write(datamodel)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("format_version")

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    format_docs_dir = input_path / args.format_version
    if not format_docs_dir.exists():
        raise ValueError(f"{format_docs_dir} does not exist")

    input_objects, output_objects = create_objects(format_docs_dir)
    # TEMPORARY FOR INSPECTION
    with open(datamodel_path / "all_objects.py", "w") as f:
        f.write("# Input Objects ----------------------------------------------------------------\n\n")
        f.write("# ------ Static ----------------------------------------------------------------\n\n")
        for name, obj in input_objects["static"].items():
            f.write(obj + "\n\n")
        f.write("# -- Timeseries ----------------------------------------------------------------\n\n")
        for name, obj in input_objects["timeseries"].items():
            f.write(obj + "\n\n")
        f.write("# Output Objects ----------------------------------------------------------------\n\n")
        f.write("# ------ Static ----------------------------------------------------------------\n\n")
        for name, obj in input_objects["static"].items():
            f.write(obj + "\n\n")
        f.write("# -- Timeseries ----------------------------------------------------------------\n\n")
        for name, obj in input_objects["timeseries"].items():
            f.write(obj + "\n\n")

    create_models(format_docs_dir, input_objects, output_objects)
