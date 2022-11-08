import abc
import argparse
import enum
import logging
from pathlib import Path
import re

from datamodel import datamodel_path, input_path

logger = logging.getLogger(__name__)


# After objects have been created, these files say how to assemble them
models = {
    ("input", "data"): [
        "static_json",
        "time_series",
        "reliability",
        "parsing_mapping"
    ],
    ("output", "data"): [
        "solution",
        "parsing_mapping"
    ]
}


def create_objects(format_docs_dir):
    input_objects = {
        "static": {},
        "staticinner": {},
        "timeseries": {},
        "reliability": {},
    }
    output_objects = {
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
        candidate = candidate.replace(" ","").replace("-","").replace("\\&","").replace(":","_")
        tmp = _split(text, r"^\\paragraph\{(.+)\}.*$")
        if "Input Attributes" in tmp:
            logger.info(f"Processing {candidate} input attributes")
            # process input attribute table
            static_obj, timeseries_obj, reliability_obj, static_inner_objs, timeseries_inner_objs, reliability_inner_objs = \
                get_objects_from_table(candidate, tmp["Input Attributes"])
            if (static_obj is None) and (timeseries_obj is None) and (reliability_obj is None):
                logger.info(f"Unable to extract input attributes for {candidate}")
            else:
                if static_obj:
                    input_objects["static"][candidate] = static_obj
                if static_inner_objs:
                    for inner_obj, inner_obj_str in static_inner_objs.items():
                        input_objects["staticinner"][inner_obj] = inner_obj_str
                if timeseries_obj:
                    input_objects["timeseries"][candidate] = timeseries_obj
                if timeseries_inner_objs:
                    for inner_obj, inner_obj_str in timeseries_inner_objs.items():
                        input_objects["timeseriesinner"][inner_obj] = inner_obj_str
                if reliability_obj:
                    input_objects["reliability"][candidate] = reliability_obj
                if reliability_inner_objs:
                    for inner_obj, inner_obj_str in reliability_inner_objs.items():
                        input_objects["reliabilityinner"][inner_obj] = inner_obj_str
        else:
            logger.info(f"No input attributes for {candidate}")
        
        if "Output Attributes" in tmp:
            logger.info(f"Processing {candidate} output attributes")
            # process output attribute table
            static_obj, timeseries_obj, reliability_obj, static_inner_objs, timeseries_inner_objs, reliability_inner_objs = \
                get_objects_from_table(candidate, tmp["Output Attributes"])
            if (static_obj is None) and (timeseries_obj is None) and (reliability_obj is None):
                logger.info(f"Unable to extract output attributes for {candidate}")
            else:
                if static_obj:
                    output_objects["static"][candidate] = static_obj
                if static_inner_objs:
                    for inner_obj, inner_obj_str in static_inner_objs.items():
                        output_objects["staticinner"][inner_obj] = inner_obj_str
                if timeseries_obj:
                    output_objects["timeseries"][candidate] = timeseries_obj
                if timeseries_inner_objs:
                    for inner_obj, inner_obj_str in timeseries_inner_objs.items():
                        output_objects["timeseriesinner"][inner_obj] = inner_obj_str
                if reliability_obj:
                    output_objects["reliability"][candidate] = reliability_obj
                if reliability_inner_objs:
                    for inner_obj, inner_obj_str in reliability_inner_objs.items():
                        output_objects["reliabilityinner"][inner_obj] = inner_obj_str

        else:
            logger.info(f"No output attributes for {candidate}")

    return input_objects, output_objects


def get_objects_from_table(object_name, astr):
    static_result = ""
    static_conditional_result = ""
    timeseries_result = ""
    timeseries_conditional_result = ""
    reliability_result = ""
    static_inner_objects = {}
    timeseries_inner_objects = {}
    reliability_inner_objects = {}
    static_conditional_elements = {}
    timeseries_conditional_elements = {}

    # Some descriptions in the table overflow onto the following line. 
    # This bit of code joins those lines together.
    all_lines = astr.split('\n')
    all_lines_new = []
    for ln_cnt in range(len(all_lines)-1,-1,-1): 
        ln = all_lines[ln_cnt]
        if ln.strip().startswith('&'):
            desc = ln.split('&')[1]
            prev_line = all_lines[ln_cnt-1]
            prev_line_fields = prev_line.split('&')
            prev_line_fields[1]+=desc
            updated_prev_line = '&'.join(prev_line_fields)
            all_lines[ln_cnt -1] = updated_prev_line
        else:
            all_lines_new.append(ln)

    all_lines_new.reverse()
    all_lines = all_lines_new

    # Create objects that are of json type
    all_lines_new  = []
    ln_cnt = 0
    while ln_cnt < len(all_lines):
        ln = all_lines[ln_cnt]
        if '[Inner Attributes]' in ln:
            m = re.match(".*\{\\\\tt\S* (.+)\}.*",ln)
            if not m:
                logger.warning(f"Unable to extract inner attributes from {ln!r}")
                ln_cnt+=1
                continue
            inner_attribute = m.group(1).replace("\\_", "_")
            inner_attribute_formatted = object_name+'_'+inner_attribute
            inner_attribute_class = object_name+inner_attribute.replace("_"," ").title().replace(" ","")
            inner_attribute_array = object_name+'_'+'Array of '+inner_attribute

            types_map[inner_attribute_formatted] = inner_attribute_class
            types_map[inner_attribute_array] = "List["+inner_attribute_class+"]"
            internal_result = f"class {inner_attribute_class}Base(BidDSJsonBaseModel):\n"
            ln_cnt +=2 # skip the new line
            while True: #This is bad practice...
                ln = all_lines[ln_cnt]
                if '\hline' in ln:
                    break
                sec,field = parse_field(ln,object_name)
                if field:
                    internal_result += field
                else:
                    logger.warning(f"unable to parse line {ln!r}")
                ln_cnt+=1

            if sec == 'S' or sec == 'B':
                static_inner_objects[inner_attribute_class] = internal_result
            if sec == 'T' or sec == 'B':
                timeseries_inner_objects = internal_result
            if sec == 'C':
                reliability_inner_objects = internal_result

        elif 'Conditional Attributes]' in ln:
            m = re.match(".*\{\\\\tt\S* (.+)\}.*",ln)
            if not m:
                logger.warning(f"Unable to extract conditional attributes from {ln!r}")
                ln_cnt+=1
                continue
            conditional_attribute = m.group(1).replace("\\_", "_")

            ln_cnt +=2 # skip the new line

            while True: #This is bad practice...
                ln = all_lines[ln_cnt]
                if '\hline' in ln:
                    break
                sec,field = parse_field(ln,object_name,is_conditional= True)
                if field:
                    field_name = field.strip().split(':')[0]
                    if sec == 'S' or sec == 'B':
                        static_conditional_elements[field_name] = conditional_attribute
                        static_conditional_result += field
                    if sec == 'T' or sec == 'B':
                        timeseries_conditional_elements[field_name] = conditional_attribute
                        timeseries_conditional_result += field
                    if False: #TODO: Find a way to manage the conditional elements based on the conditional_attribute
                        timeseries_result += conditional_result
                        static_result += conditional_result
                        # no conditional reliability results
                else:
                    logger.warning(f"unable to parse line {ln!r}")
                ln_cnt+=1


        else:
            all_lines_new.append(ln)

        ln_cnt+=1

    static_result += f"class {object_name}Base(BidDSJsonBaseModel):\n"
    timeseries_result += f"class {object_name}Base(BidDSJsonBaseModel):\n"
    reliability_result += f"class {object_name}Base(BidDSJsonBaseModel):\n"
    has_static = False; has_timeseries = False; has_reliability = False

    table_started = False; expect_meta = True
    for ln in all_lines_new:
        if not table_started:
            if ln.startswith("\\begin{tabular}"):
                table_started = True
            continue
        if ln.startswith("\\begin{tabular}"):
            expect_meta = True
            continue
        if ln.startswith("\\end{tabular}"):
            expect_meta = False
            continue
        if ln.strip().startswith("%"): # comment character
            continue
        if ln.strip() == "\\hline":
            expect_meta = True
            continue
        if ln.strip().startswith("{\\tt"):
            sec, field = parse_field(ln,object_name)
            if field:
                if sec == "S":
                    static_result += field
                    has_static = True
                elif sec == "T":
                    timeseries_result += field
                    has_timeseries = True
                elif sec == "C":
                    reliability_result += field
                    has_reliability = True
                else:
                    assert sec == "B", repr(sec)
                    static_result += field
                    timeseries_result += field
        elif expect_meta:
            meta = ln.split("&")[0].strip()
            static_result += f"\n    # {meta}\n"
            timeseries_result += f"\n    # {meta}\n"
            continue

    static_result += static_conditional_result # fix bug here - misspelling conditional - eh, not actually a bug, just confusing
    timeseries_result += timeseries_conditional_result

    if not has_static:
        static_result = None
        static_inner_objects = None
    else:
        if len(static_conditional_elements) > 0:
            for conditional_element, dependency in static_conditional_elements.items():
                # values is a dict. need to use values.get(key), not values[key]
                #static_result+= f"""\n    @root_validator(pre=False)\n    def check_conditional_{conditional_element}(cls, values):\n        if values["{dependency}"] == 1 and values["{conditional_element}"] is None:\n             raise ValueError("Conditional element {conditional_element} is missing when {dependency} is 1")\n        if values["{dependency}"] != 1 and values["{conditional_element}"] is not None:\n             raise ValueError("Conditional element {conditional_element} is present when {dependency} is not 1")\n        return values"""
                static_result+= f"""\n    @root_validator(pre=False)\n    def check_conditional_{conditional_element}(cls, values):\n        if values.get("{dependency}") is not None and values.get("{dependency}") == 1 and values.get("{conditional_element}") is None:\n             raise ValueError("Conditional element {conditional_element} is missing when {dependency} is 1")\n        if values.get("{dependency}") is not None and values.get("{dependency}") != 1 and values.get("{conditional_element}") is not None:\n             raise ValueError("Conditional element {conditional_element} is present when {dependency} is not 1")\n        return values"""
                             
    if not has_timeseries:
        timeseries_result = None
        timeseries_inner_objects = None
    else:
        if len(timeseries_conditional_elements) > 0:
            for conditional_element, dependency in timeseries_conditional_elements.items():
                static_result+= f"""\n    @root_validator(pre=False)\n    def check_conditional_{conditional_element}(cls, values):\n        if values.get("{dependency}") is not None and values.get("{dependency}") == 1 and values.get("{conditional_element}") is None:\n             raise ValueError("Conditional element {conditional_element} is missing when {dependency} is 1")\n        if values.get("{dependency}") is not None and values.get("{dependency}") != 1 and values.get("{conditional_element}") is not None:\n             raise ValueError("Conditional element {conditional_element} is present when {dependency} is not 1")\n        return values"""

    if not has_reliability:
        reliability_result = None
        reliability_inner_objects = None

    if table_started:
        return (static_result, timeseries_result, reliability_result, static_inner_objects, timeseries_inner_objects, reliability_inner_objects) 
    return (None, None, None, None, None, None)


# Gets extended with internal json objects
types_map = {
    "Array of Int": "List[StrictInt]",
    "Array of Float": "List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)]",
    #"Array of Binary": "List[bool]",
    "Array of Binary": "List[conint(ge=0, le=1, strict=True)]",
    "Array of String": "List[str]",
    "Array of Float Float": "List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]]",
    "Array of Array of Array of Float Float": "List[List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]]]",
    "Array of Float Float Float": "List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]]",
    "Array of Float Float Int": "List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False), StrictInt]]",
    "String": "str",
    "Timestamp": "str",
    "Int": "StrictInt",
    "Float": "confloat(gt=-float('inf'), lt=float('inf'), strict=False)",
    #"Binary": "bool",
    "Binary": "conint(ge=0, le=1, strict=True)",
}

def parse_field(ln,object_name,is_conditional=False):
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
    desc = m.group(1); type_name = m.group(2)

    tmp = type_name.split(',')
    if not tmp[0].strip().startswith('String:'):
        type_name = tmp[0].strip().replace("\\_", "_")
    if len(tmp) > 1:
        # TODO: Put units somewhere in the Pydantic model
        units = ','.join(tmp[1:]).lstrip()

    choices = None
    if type_name in types_map:
        type_name = types_map[type_name]
    elif object_name+'_'+type_name in types_map:
        type_name = types_map[object_name+'_'+type_name]

    else:
        if type_name.startswith("String:"):
            # choices list
            choices = type_name.split(":")[1].strip().split(", ")
            choices = [choice.strip().replace("\\_","_") for choice in choices]
            # TODO: Consider turning choices into an Enum and then setting type_name 
            # to be that Enum
            type_name = "str"
        elif type_name.startswith("Binary:"):
            type_name = "bool"
        else:
            logger.warning(f"Unable to extract type_name from {type_name!r}")
            return sec, ""
    
    if req.lower().strip() == "n" or is_conditional:
        type_name = f"Optional[{type_name}]"

    sep = "," if choices else ""
    
    result = f"""
    {name}: {type_name} = Field(
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
    for names, files in models.items():
        object_refs = input_objects if names[0] == 'input' else output_objects
        object_store = {}
        imports = set()
        schema_object = None

        for file in files:
            object_ref = None
            object_preamble = f"datamodel.{names[0]}"
            if file.startswith("static"):
                object_ref = object_refs["static"]
                object_preamble += ".static"
            elif file.startswith("time_series"):
                object_ref = object_refs["timeseries"]
                object_preamble += ".timeseries"
            elif file.startswith("reliability"):
                object_ref = object_refs["reliability"]
                object_preamble += ".reliability"
            elif file.startswith("solution"):
                object_ref = object_refs["timeseries"]
                object_preamble += ".timeseries"
            elif file.startswith("parsing_mapping"):
                object_ref = object_store
                object_preamble = ""
            if object_preamble:
                imports.add(object_preamble)


            with open(format_docs_dir / f"{file}.tex", encoding="utf8") as f:
                file_text = f.read()

            subsections = _split(file_text, r"^\\subsection\{(.+)\}\s*$")

            if object_preamble:
                orig_name = list(subsections.keys())[0] 
                object_name = orig_name.title().replace(" ","")
                logger.info(f"Creating {object_name} object")
                obj = get_object_from_subsection(object_name, 
                    subsections[orig_name], object_ref, object_preamble) if object_ref else None
                if obj is None:
                    logger.warning(f"Unable to parse {object_name} from first "
                        f"subsection of {file}.tex")
                    continue
                object_store[object_name] = obj
            else:
                # write out sections as their own file
                sections_names = list(names[:-1]) + ["sections"]
                write_file(datamodel_path, sections_names, object_store, is_base=True, imports=imports)
                object_store = {}

                # now compose the overall file
                orig_name = f"{names[0].title()} Data File"
                if not orig_name in subsections:
                    logger.warning(f"Unable to find subsection {orig_name}")
                    continue
                object_name = orig_name.title().replace(" ","")
                logger.info(f"Creating {object_name} object")
                obj = get_object_from_subsection(
                    object_name, 
                    subsections[orig_name], 
                    object_ref, 
                    object_preamble, 
                    is_base=True,
                    is_schema=True) if object_ref else None
                if obj is None:
                    logger.warning(f"Unable to parse {object_name} from first "
                        f"subsection of {file}.tex")
                    continue
                object_store[object_name] = obj

        # write out the overall file
        write_file(datamodel_path, names, object_store, is_base=True, imports=[f"from datamodel.{'.'.join(sections_names)} import *"])


def get_object_from_subsection(object_name, astr, object_ref, object_preamble, is_base=True, is_schema=False):
    if is_base:
        base = 'Base'
    else:
        base = ''
    if object_preamble !='':
        object_preamble+='.'
    result = f"class {object_name}{base}(BidDSJsonBaseModel):\n"

    if is_schema:
        result += f"""
    class Config:
        title = "{object_name}"
        """

    obj_ref_map = {key.lower(): key for key in object_ref.keys()}
    obj_ref_map_keys = list(obj_ref_map.keys()) # TO avoid modifying dictionary
    for key in obj_ref_map_keys:

        # Provided due to inconsistencies in the naming of subsections in section 2 and json objects in sections 3 and 4
        if key == "violationcostsparameters":
            obj_ref_map["violationcost"] = obj_ref_map.pop("violationcostsparameters")
        elif key == "dispatchabledevices_simpleproducingconsumingdevices":
            obj_ref_map["simpledispatchabledevice"] = obj_ref_map.pop("dispatchabledevices_simpleproducingconsumingdevices")
        elif key == "dispatchabledevices_multimodeproducingconsumingdevices":
            obj_ref_map["multimodedispatchabledevice"] = obj_ref_map.pop("dispatchabledevices_multimodeproducingconsumingdevices")
        elif key == "actransmissionline":
            obj_ref_map["acline"] = obj_ref_map.pop("actransmissionline")
        elif key == "activezonalreserverequirementsviolationcosts":
            obj_ref_map["activezonalreserve"] = obj_ref_map.pop("activezonalreserverequirementsviolationcosts") 
        elif key == "reactivezonalreserverequirementsviolationcosts":
            obj_ref_map["reactivezonalreserve"] = obj_ref_map.pop("reactivezonalreserverequirementsviolationcosts") 
        elif key == "subdeviceunitsformultimodeproducingconsumingdevices":
            obj_ref_map["subdevice"] = obj_ref_map.pop("subdeviceunitsformultimodeproducingconsumingdevices")        
        # TODO: storage devices
        # TODO: development

    def get_dict_str(adict):
        items = [f"{k}: {v}" for k, v in adict.items()]
        result = "{\n  "
        result += "\n  ".join(items)
        result += "\n}"
        return result

    # first try to parse form itemized list
    items_started = False; found_object = None; contains_objects = False
    for ln in astr.split("\n"):
        if not items_started:
            if ln.startswith("\\begin{itemize}"):
                items_started = True
            continue
        if ln.startswith("\\end{itemize}"):
            break
        if ln.strip().startswith("%"): # comment character
            continue
        if ln.strip().startswith("\\item"):
            found_object = None
            m = re.match(r".+\\texttt\{(.+)\}.+(object|array).*", ln.strip())
            if m:
                contains_objects = True
                name = m.group(1).replace("\"","").replace("\\_","_").replace(":","_").replace("-","_")
                object_type = m.group(2)
                key = name.replace("_","").replace("-","")
                if key in obj_ref_map:
                    found_object = (name, obj_ref_map[key], object_type)
                    continue
            logger.warning(f"Unable to locate object in {ln.strip()}.")
            if m:
                logger.warning(f"Was able to parse object name {name} "
                    f"({m.group(1)}), but key {key} not in map:\n"
                    f"{get_dict_str(obj_ref_map)}")
        if found_object:
            name = found_object[0]
            object_type = found_object[2]
            type = f"{object_preamble}{found_object[1]}"
            #if "array" in ln.strip():
            if object_type == 'array':
                #name += "es" if name.endswith("s") else "s"
                type = f"List[{type}]"
            result += f"""
    {name}: {type} = Field(
        title = "{name}"
    )\n"""
            found_object = None
    
    if items_started and contains_objects:
        return result

    # now try to parse from verbatim section
    verbatim_started = False; found_object = None; contains_objects = False
    for ln in astr.split("\n"):
        if not verbatim_started:
            if ln.startswith("\\begin{verbatim}"):
                verbatim_started = True
            continue
        if ln.startswith("\\end{verbatim}"):
            break
        m = re.match(r"(.+): [\{\[].*", ln.strip())
        if m:
            contains_objects = True
            name = m.group(1).replace("\"","").replace("”","")
            key = name.replace("_","")
            if key in obj_ref_map:
                found_object = (name, obj_ref_map[key])
            else:
                logger.warning(f"Was able to parse object name {name} "
                    f"({m.group(1)}), but key {key} not in map:\n"
                    f"{get_dict_str(obj_ref_map)}")
        if found_object:
            name = found_object[0]
            type = found_object[1]+'Base'
            if object_preamble:
                type = f"{object_preamble}{type}"
            result += f"""
    {name}: {type} = Field(
        title = "{name}"
    )\n"""
            found_object = None

    if contains_objects:
        return result

    return None


def write_file(datamodel_path, names, objects, is_base = True, imports = []):
    n = len(names)
    p = datamodel_path
    prefix = ".".join(names)
    for i, name in enumerate(names):
        if i == n-1:
            if is_base:
                p = p / f"{name}base.py"
            else:
                p = p / f"{name}.py"
            break
        p = p / name
        if not p.exists():
            p.mkdir()
            (p / "__init__.py").touch()
    
    # write the base models
    with open(p, "w") as f:
        f.write(
"""import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel\n""")
        for to_import in imports:
            if " " in to_import:
                f.write(f"{to_import}\n")
            else:
                f.write(f"import {to_import}\n")

        f.write("\n")
        for name, obj in objects.items():
            f.write(obj + "\n\n")

    # write template for derived models
    if is_base:
        pp = p.parent / f"__{p.stem[:-4]}.py"
        with open(pp, "w") as f:
            f.write(
f"""import logging
from datamodel.{prefix}base import *\n""")
            f.write("\n")
            for name in objects.keys():
                f.write(f"class {name}({name}Base): pass" + "\n\n")

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("format_version")

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    format_docs_dir = input_path / args.format_version
    if not format_docs_dir.exists():
        format_docs_dir_orig = format_docs_dir
        format_docs_dir = Path(args.format_version).resolve()
        if not format_docs_dir.exists():
            msg = f"format_docs_dir not found. {format_docs_dir_orig} does not exist and {format_docs_dir} does not exist"
            raise ValueError(msg)
    #print("format_docs_dir: {}".format(format_docs_dir))

    input_objects, output_objects = create_objects(format_docs_dir)
    object_files = {
        ("input", "static"): (input_objects["static"], ["from datamodel.input.staticinner import *"]),
        ("input", "staticinner"): (input_objects["staticinner"], []),
        ("input", "timeseries"): (input_objects["timeseries"], []),
        ("input", "reliability"): (input_objects["reliability"], []),
        ("output", "timeseries"): (output_objects["timeseries"], []),
    }
    for dirs, data in object_files.items():
        objs, imports = data
        is_base = True
        if 'inner' in dirs[1]:
            is_base = True
            for key in list(objs.keys()):
                objs[key.replace('Base','')] = objs.pop(key)
        write_file(datamodel_path, dirs, objs, is_base, imports=imports)

    create_models(format_docs_dir, input_objects, output_objects)

    # write out schemas
    p = datamodel_path / "schemas"
    if not p.exists():
        p.mkdir()

    from datamodel.input.data import InputDataFile
    InputDataFile.save_schema(p / "input_data_file_schema.json", indent=4)

    from datamodel.output.data import OutputDataFile
    OutputDataFile.save_schema(p / "output_data_file_schema.json", indent=4)
