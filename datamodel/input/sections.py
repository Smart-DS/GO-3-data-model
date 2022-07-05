import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
import datamodel.input.contingencybase
import datamodel.input.timeseriesbase
import datamodel.input.staticbase

class NetworkBase(BidDSJsonBaseModel):

    general: datamodel.input.staticbase.GeneralBase = Field(
        title = "general"
    )

    violation_cost: datamodel.input.staticbase.ViolationCostsParametersBase = Field(
        title = "violation_cost"
    )

    bus: List[datamodel.input.staticbase.BusBase] = Field(
        title = "bus"
    )

    shunt: List[datamodel.input.staticbase.ShuntBase] = Field(
        title = "shunt"
    )

    simple_dispatchable_device: List[datamodel.input.staticbase.DispatchableDevices_SimpleProducingConsumingDevicesBase] = Field(
        title = "simple_dispatchable_device"
    )

    ac_line: List[datamodel.input.staticbase.ACTransmissionLineBase] = Field(
        title = "ac_line"
    )

    two_winding_transformer: List[datamodel.input.staticbase.TwoWindingTransformerBase] = Field(
        title = "two_winding_transformer"
    )

    dc_line: List[datamodel.input.staticbase.DCLineBase] = Field(
        title = "dc_line"
    )

    active_zonal_reserve: List[datamodel.input.staticbase.ActiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "active_zonal_reserve"
    )

    reactive_zonal_reserve: List[datamodel.input.staticbase.ReactiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "reactive_zonal_reserve"
    )


class TimeSeriesInputBase(BidDSJsonBaseModel):

    general: datamodel.input.timeseriesbase.GeneralBase = Field(
        title = "general"
    )

    simple_dispatchable_device: List[datamodel.input.timeseriesbase.DispatchableDevices_SimpleProducingConsumingDevicesBase] = Field(
        title = "simple_dispatchable_device"
    )

    active_zonal_reserve: List[datamodel.input.timeseriesbase.ActiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "active_zonal_reserve"
    )

    reactive_zonal_reserve: List[datamodel.input.timeseriesbase.ReactiveZonalReserveRequirementsViolationCostsBase] = Field(
        title = "reactive_zonal_reserve"
    )


class ContingencyBase(BidDSJsonBaseModel):

    contingency: datamodel.input.contingencybase.ContingencyBase = Field(
        title = "contingency"
    )


