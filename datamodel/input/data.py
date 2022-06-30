import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
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


