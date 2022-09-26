import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
from datamodel.output.sections import *

class OutputDataFileBase(BidDSJsonBaseModel):

    class Config:
        title = "OutputDataFile"
        
    time_series_output: TimeSeriesOutput = Field(
        title = "time_series_output"
    )


