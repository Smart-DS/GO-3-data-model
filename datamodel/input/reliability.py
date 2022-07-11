import logging
from pydantic import root_validator, validator
from datamodel.input.reliabilitybase import *

class Contingency(ContingencyBase):

    @validator("components")
    def num_components_eq_q(cls, data):

        if not (len(data) == 1):
            msg = "fails {} == 1. {}: {}".format(
                "len(components)", "len(components)", len(data))
            raise ValueError(msg)
        return data            
