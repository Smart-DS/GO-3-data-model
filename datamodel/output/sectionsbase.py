import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
import datamodel.output.timeseries

class TimeSeriesOutputBase(BidDSJsonBaseModel):

    bus: List[datamodel.output.timeseries.Bus] = Field(
        title = "bus"
    )

    shunt: List[datamodel.output.timeseries.Shunt] = Field(
        title = "shunt"
    )

    simple_dispatchable_device: List[datamodel.output.timeseries.DispatchableDevices_SimpleProducingConsumingDevices] = Field(
        title = "simple_dispatchable_device"
    )

    ac_line: List[datamodel.output.timeseries.ACTransmissionLine] = Field(
        title = "ac_line"
    )

    two_winding_transformer: List[datamodel.output.timeseries.TwoWindingTransformer] = Field(
        title = "two_winding_transformer"
    )

    dc_line: List[datamodel.output.timeseries.DCLine] = Field(
        title = "dc_line"
    )


