import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
import datamodel.input.static
import datamodel.input.timeseries

class Network(BidDSJsonBaseModel):

    general: datamodel.input.static.General = Field(
        title = "general"
    )

    violation_cost: datamodel.input.static.ViolationCostsParameters = Field(
        title = "violation_cost"
    )

    buses: List[datamodel.input.static.Bus] = Field(
        title = "buses"
    )

    shunts: List[datamodel.input.static.Shunt] = Field(
        title = "shunts"
    )

    simple_dispatchable_devices: List[datamodel.input.static.DispatchableDevices_SimpleProducingConsumingDevices] = Field(
        title = "simple_dispatchable_devices"
    )

    multi_mode_dispatchable_devices: List[datamodel.input.static.DispatchableDevices_MultimodeProducingConsumingDevices] = Field(
        title = "multi_mode_dispatchable_devices"
    )

    sub_devices: List[datamodel.input.static.SubdeviceUnitsforMultiModeProducingConsumingDevices] = Field(
        title = "sub_devices"
    )

    ac_lines: List[datamodel.input.static.ACTransmissionLine] = Field(
        title = "ac_lines"
    )

    two_winding_transformers: List[datamodel.input.static.TwoWindingTransformer] = Field(
        title = "two_winding_transformers"
    )

    dc_lines: List[datamodel.input.static.DCLine] = Field(
        title = "dc_lines"
    )

    active_regional_reserves: List[datamodel.input.static.RegionalReserves] = Field(
        title = "active_regional_reserves"
    )

    reactive_regional_reserves: List[datamodel.input.static.RegionalReserves] = Field(
        title = "reactive_regional_reserves"
    )


class TimeSeriesInput(BidDSJsonBaseModel):

    general: datamodel.input.timeseries.General = Field(
        title = "general"
    )

    simple_dispatchable_devices: List[datamodel.input.timeseries.DispatchableDevices_SimpleProducingConsumingDevices] = Field(
        title = "simple_dispatchable_devices"
    )

    multi_mode_dispatchable_devices: List[datamodel.input.timeseries.DispatchableDevices_MultimodeProducingConsumingDevices] = Field(
        title = "multi_mode_dispatchable_devices"
    )

    subdevices: List[datamodel.input.timeseries.SubdeviceUnitsforMultiModeProducingConsumingDevices] = Field(
        title = "subdevices"
    )

    active_regional_reserves: List[datamodel.input.timeseries.RegionalReserves] = Field(
        title = "active_regional_reserves"
    )

    reactive_regional_reserves: List[datamodel.input.timeseries.RegionalReserves] = Field(
        title = "reactive_regional_reserves"
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


