import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel

class BusInitialStatusBase(BidDSJsonBaseModel):

    vm: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "vm",
        description = "Bus voltage magnitude in p.u. "
    )

    va: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "va",
        description = "Bus voltage angle     in radian "
    )


class ShuntInitialStatusBase(BidDSJsonBaseModel):

    step: StrictInt = Field(
        title = "step",
        description = "Number of step "
    )


class DispatchableDevices_SimpleProducingConsumingDevicesInitialStatusBase(BidDSJsonBaseModel):

    on_status: conint(ge=0, le=1, strict=True) = Field(
        title = "on_status",
        description = "On status indicator for initial time step "
    )

    p: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p",
        description = "{ (Case: producer) Active production for initial time step in p.u. (Float) } { (Case: consumer) Active consumption for initial time step in p.u. "
    )

    q: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "q",
        description = "{ (Case: producer) Reactive production for initial time step in p.u. (Float) } { (Case: consumer) Reactive consumption for initial time step in p.u. "
    )

    accu_down_time: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "accu_down_time",
        description = "Accumulated down time in hr "
    )

    accu_up_time: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "accu_up_time",
        description = "Accumulated up time in hr "
    )


class ACTransmissionLineInitialStatusBase(BidDSJsonBaseModel):

    on_status: conint(ge=0, le=1, strict=True) = Field(
        title = "on_status",
        description = "Connection status "
    )


class TwoWindingTransformerInitialStatusBase(BidDSJsonBaseModel):

    on_status: conint(ge=0, le=1, strict=True) = Field(
        title = "on_status",
        description = "Connection status "
    )

    tm: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "tm",
        description = "Off-nominal tap ratio in p.u. "
    )

    ta: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "ta",
        description = "Phase shifting angle in radian "
    )


class DCLineInitialStatusBase(BidDSJsonBaseModel):

    pdc_fr: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "pdc_fr",
        description = "Active power flow in p.u. "
    )

    qdc_fr: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "qdc_fr",
        description = "Reactive power flow, from bus in p.u. "
    )

    qdc_to: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "qdc_to",
        description = "Reactive power flow, to bus in p.u. "
    )


