import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
import datamodel.input.static
import datamodel.input.contingency
import datamodel.input.timeseries

class NetworkBase(BidDSJsonBaseModel):

    general: datamodel.input.static.GeneralBase = Field(
        title = "general"
    )

    violation_cost: datamodel.input.static.ViolationCostsParametersBase = Field(
        title = "violation_cost"
    )

    bus: List[datamodel.input.static.BusBase] = Field(
        title = "bus"
    )

    shunt: List[datamodel.input.static.ShuntBase] = Field(
        title = "shunt"
    )

    simple_dispatchable_device: List[datamodel.input.static.DispatchableDevices_SimpleProducingConsumingDevicesBase] = Field(
        title = "simple_dispatchable_device"
    )

    ac_line: List[datamodel.input.static.ACTransmissionLineBase] = Field(
        title = "ac_line"
    )

    two_winding_transformer: List[datamodel.input.static.TwoWindingTransformerBase] = Field(
        title = "two_winding_transformer"
    )

    dc_line: List[datamodel.input.static.DCLineBase] = Field(
        title = "dc_line"
    )

    active_zonal_reserve: List[datamodel.input.static.ActiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "active_zonal_reserve"
    )

    reactive_zonal_reserve: List[datamodel.input.static.ReactiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "reactive_zonal_reserve"
    )


class TimeSeriesInputBase(BidDSJsonBaseModel):

    general: datamodel.input.timeseries.GeneralBase = Field(
        title = "general"
    )

    simple_dispatchable_device: List[datamodel.input.timeseries.DispatchableDevices_SimpleProducingConsumingDevicesBase] = Field(
        title = "simple_dispatchable_device"
    )

    active_zonal_reserve: List[datamodel.input.timeseries.ActiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "active_zonal_reserve"
    )

    reactive_zonal_reserve: List[datamodel.input.timeseries.ReactiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "reactive_zonal_reserve"
    )


class ContingencyInputBase(BidDSJsonBaseModel):

    contingency: List[datamodel.input.contingency.ContingencyBase] = Field(
        title = "contingency"
    )


