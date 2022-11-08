import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
import datamodel.input.reliability
import datamodel.input.static
import datamodel.input.timeseries

class NetworkBase(BidDSJsonBaseModel):

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


class TimeSeriesInputBase(BidDSJsonBaseModel):

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


class ReliabilityBase(BidDSJsonBaseModel):

    contingency: List[datamodel.input.reliability.Contingency] = Field(
        title = "contingency"
    )


