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
    input_objects = {}; output_objects = {};
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
        tmp = _split(text, r"^\\paragraph\{(.+)\}\s*$")
        if "Input Attributes" in tmp:
            # process input attribute table
            obj = get_object_from_table(candidate, tmp["Input Attributes"])
            if obj is not None:
                input_objects[candidate] = obj
        
        if "Output Attributes" in tmp:
            # process output attribute table
            obj = get_object_from_table(candidate, tmp["Output Attributes"])
            if obj is not None:
                output_objects[candidate] = obj

    return input_objects, output_objects


def get_object_from_table(object_name, astr):
    result = f"class {object_name}(BidDSJsonBaseModel):\n"
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
            result += parse_field(ln)
        elif expect_meta:
            meta = ln.split("&")[0].strip()
            result += f"\n    # {meta}\n"
            continue

    return result if table_started else None


types_map = {
    "Int": "int",
    "Float": "float",
    "\\$/p.u.": "float"
}

def parse_field(ln):
    name, desc, req, sec, sym = ln.split("&")
    
    # get name
    m = re.match("\{\\\\tt\S* (.+)\}", name.strip())
    if not m:
        logger.warning(f"Unable to extract name from {name!r}")
        return ""
    name = m.group(1).replace("\\_", "_")

    # get description and type
    m = re.match("(.*)\((.*)\)", desc.strip())
    if not m:
        logger.warning(f"Unable to partition {desc!r} into description and type")
        return ""
    desc = m.group(1); type = m.group(2)

    if not type in types_map:
        logger.warning(f"Unable to extract type from {desc!r}")
        return ""
    type = types_map[type]
    
    result = f"""
    {name}: {type} = Field(
        title = "{name}",
        description = "{desc}"
    )\n"""
    return result

    
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

    logging.basicConfig()

    format_docs_dir = input_path / args.format_version
    if not format_docs_dir.exists():
        raise ValueError(f"{format_docs_dir} does not exist")

    input_objects, output_objects = create_objects(format_docs_dir)
    # TEMPORARY FOR INPECTION
    with open(datamodel_path / "all_objects.py", "w") as f:
        f.write("# Input Objects ----------------------------------------------------------------\n\n")
        for name, obj in input_objects.items():
            f.write(obj + "\n\n")
        f.write("# Output Objects ----------------------------------------------------------------\n\n")
        for name, obj in input_objects.items():
            f.write(obj + "\n\n")

    create_models(format_docs_dir, input_objects, output_objects)
