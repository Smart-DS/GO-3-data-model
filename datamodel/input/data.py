import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError, validator
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
from datamodel.input.sections import *

class InputDataFile(BidDSJsonBaseModel):

    class Config:
        title = "InputDataFile"
        
    network: NetworkBase = Field(
        title = "network"
    )

    timeseriesinput: TimeSeriesInputBase = Field(
        title = "timeseriesinput"
    )

    contingency: ContingencyBase = Field(
        title = "contingency"
    )


#<<<<<<< HEAD
#class InputDataFile(InputDataFileBase):
#=======
#>>>>>>> te/latex_fixes

    # @validator("network")
    # def network_general_stop_is_after_start(cls, network):
    #     if network.general.timestamp_stop <= network.general.timestamp_start:
    #         raise ValueError("timestamp_stop must be greater than timestamp_start")
    #     # If the following 2 lines are not included, the network field is None. But we do not need this when the validator is placed in the code-written class definition.
    #     else:
    #         return network

    pass
