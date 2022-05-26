import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
import datamodel.input.timeseries
import datamodel.input.static

class Network(BidDSJsonBaseModel):

    general: datamodel.input.static.General = Field(
        title = "general"
    )

    violation_cost: datamodel.input.static.ViolationCostsParameters = Field(
        title = "violation_cost"
    )

    bus: List[datamodel.input.static.Bus] = Field(
        title = "bus"
    )

    shunt: List[datamodel.input.static.Shunt] = Field(
        title = "shunt"
    )

    simple_dispatchable_device: List[datamodel.input.static.DispatchableDevices_SimpleProducingConsumingDevices] = Field(
        title = "simple_dispatchable_device"
    )

    ac_line: List[datamodel.input.static.ACTransmissionLine] = Field(
        title = "ac_line"
    )

    two_winding_transformer: List[datamodel.input.static.TwoWindingTransformer] = Field(
        title = "two_winding_transformer"
    )

    dc_line: List[datamodel.input.static.DCLine] = Field(
        title = "dc_line"
    )

    active_zonal_reserve: List[datamodel.input.static.ActiveZonalReserveRequirementsViolationCosts] = Field(
        title = "active_zonal_reserve"
    )

    reactive_zonal_reserve: List[datamodel.input.static.ReactiveZonalReserveRequirementsViolationCosts] = Field(
        title = "reactive_zonal_reserve"
    )


class TimeSeriesInput(BidDSJsonBaseModel):

    general: datamodel.input.timeseries.General = Field(
        title = "general"
    )

    simple_dispatchable_device: List[datamodel.input.timeseries.DispatchableDevices_SimpleProducingConsumingDevices] = Field(
        title = "simple_dispatchable_device"
    )

    active_zonal_reserve: List[datamodel.input.timeseries.ActiveZonalReserveRequirementsViolationCosts] = Field(
        title = "active_zonal_reserve"
    )

    reactive_zonal_reserve: List[datamodel.input.timeseries.ReactiveZonalReserveRequirementsViolationCosts] = Field(
        title = "reactive_zonal_reserve"
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


