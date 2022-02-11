import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union

from datamodel.base import BidDSJsonBaseModel
import datamodel.input.timeseries
import datamodel.input.static

class Network(BidDSJsonBaseModel):

    general: datamodel.input.static.General = Field(
        title = "general"
    )

    buses: List[datamodel.input.static.Bus] = Field(
        title = "buses"
    )

    shunts: List[datamodel.input.static.Shunt] = Field(
        title = "shunts"
    )

    two_winding_transformers: List[datamodel.input.static.TwoWindingTransformer] = Field(
        title = "two_winding_transformers"
    )

    dc_lines: List[datamodel.input.static.DCLine] = Field(
        title = "dc_lines"
    )


class TimeSeriesInput(BidDSJsonBaseModel):

    generals: List[datamodel.input.timeseries.General] = Field(
        title = "generals"
    )


class InputDataFile(BidDSJsonBaseModel):

    class Config:
        title = "InputDataFile"
        
    network: Network = Field(
        title = "network"
    )

    time_series_input: TimeSeriesInput = Field(
        title = "time_series_input"
    )


