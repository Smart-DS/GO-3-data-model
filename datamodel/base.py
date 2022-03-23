import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

logger = logging.getLogger(__name__)


class BidDSJsonBaseModel(BaseModel):
    """Base data model for all dsgrid data models"""

    class Config:
        title = "BidDSJsonModel"
        anystr_strip_whitespace = True
        validate_assignment = True
        validate_all = True
        extra = "forbid"
        use_enum_values = False
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def load(cls, filename):
        """Load a data model from a file.
        Temporarily changes to the file's parent directory so that Pydantic
        validators can load relative file paths within the file.
        Parameters
        ----------
        filename : str
        """
        filename = Path(filename)
        base_dir = filename.parent.absolute()
        orig = os.getcwd()
        os.chdir(base_dir)
        try:
            cfg = cls(**load_data(filename.name))
            return cfg
        except ValidationError:
            logger.exception("Failed to validate %s", filename)
            raise
        finally:
            os.chdir(orig)

    def save(cls, filename):
        """
        Save a data model to a file
        TODO: Valiodate that the model matches the schema (typically an output model)
        Parameters
        ----------
        filename : str
        """
        filename = Path(filename)
        base_dir = filename.parent.absolute()
        orig = os.getcwd()
        os.chdir(base_dir)
        try:
            # TODO: Check if this validates. If not do a validation
            json_model = self.json()
            with open(filesname.name,'w') as file_pointer:
                json.dump(json_model,file_pointer,indent=4)
        except ValidationError:
            logger.exception("Failed to validate %s", filename)
        except IOError:
            raise(f"Problem writing file {filename}")


    @classmethod
    def schema_json(cls, by_alias=True, indent=None) -> str:
        data = cls.schema(by_alias=by_alias)
        return json.dumps(data, indent=indent, cls=ExtendedJSONEncoder)

    @classmethod
    def save_schema(cls, filename, by_alias=True, indent=None):
        with open(filename, 'w') as f:
            f.write(cls.schema_json(by_alias=by_alias, indent=indent))


class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return isoformat(obj)
        if isinstance(obj, timedelta):
            return timedelta_isoformat(obj)

        return json.JSONEncoder.default(self, obj)

# TEMPORARY: Initial hand-written example. Delete when have new framework working.

# # An Option: Translate formulation schema into Pydantic models, can output 
# # overall formulation as json schema if that's helpful for others.
# # Question: Are there other/better options we should consider?

# class Generator(BidDSJsonBaseModel):

#     uid: str = Field(
#         title="uid"
#     )
#     bus: str = Field(
#         title="bus"
#     )
#     vm_setpoint: float = Field(
#         title="vm_setpoint"
#     )


# class Network(BidDSJsonBaseModel):

#     generators: List[Generator] = Field(
#         title="generators"
#     )


# class Scenario(BidDSJsonBaseModel): pass


# class Model(BidDSJsonBaseModel):

#     network: Network = Field(
#         title="network"
#     )
#     scenario: Scenario = Field(
#         title="scenario"
#     )


def load_data(filename, **kwargs):
    """Load data from the file.
    Supports JSON, TOML, or custom via kwargs.
    Parameters
    ----------
    filename : str
    Returns
    -------
    dict
    """
    with open(filename) as f_in:
        try:
            data = json.load(f_in)
        except Exception:
            logger.exception("Failed to load data from %s", filename)
            raise

    logger.debug("Loaded data from %s", filename)
    return data