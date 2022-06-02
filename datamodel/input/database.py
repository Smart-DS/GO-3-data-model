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

class InputDataFileBase(BidDSJsonBaseModel):

    class Config:
        title = "InputDataFile"
        
    network: Network = Field(
        title = "network"
    )

    time_series_input: TimeSeriesInput = Field(
        title = "time_series_input"
    )

