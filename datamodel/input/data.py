import logging
from pydantic import validator

from datamodel.input.database import *

class InputDataFile(InputDataFileBase):

    # @validator("network")
    # def network_general_stop_is_after_start(cls, network):
    #     if network.general.timestamp_stop <= network.general.timestamp_start:
    #         raise ValueError("timestamp_stop must be greater than timestamp_start")
    #     # If the following 2 lines are not included, the network field is None. But we do not need this when the validator is placed in the code-written class definition.
    #     else:
    #         return network

    pass
