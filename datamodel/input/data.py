import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator
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

    time_series_input: TimeSeriesInputBase = Field(
        title = "time_series_input"
    )

    contingency: ContingencyInputBase = Field(
        title = "contingency"
    )


