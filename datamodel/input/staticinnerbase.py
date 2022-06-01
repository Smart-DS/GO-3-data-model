import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel

class BusInitialStatusBase(BidDSJsonBaseModel):

    vm: float = Field(
        title = "vm",
        description = "Bus voltage magnitude "
    )

    va: float = Field(
        title = "va",
        description = "Bus voltage angle     "
    )


class ShuntInitialStatusBase(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
        description = "On-off status "
    )

    step: int = Field(
        title = "step",
        description = "Number of step "
    )


class DispatchableDevices_SimpleProducingConsumingDevicesInitialStatusBase(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
        description = "On status indicator for initial time step "
    )

    p: float = Field(
        title = "p",
        description = "{ (Case: producer) Active production for initial time step (Float, p.u.) } { (Case: consumer) Active consumption for initial time step "
    )

    q: float = Field(
        title = "q",
        description = "{ (Case: producer) Reactive production for initial time step (Float, p.u.) } { (Case: consumer) Reactive consumption for initial time step "
    )

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time "
    )


class ACTransmissionLineInitialStatusBase(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
        description = "Connection status "
    )


class TwoWindingTransformerInitialStatusBase(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
        description = "Connection status "
    )

    tm: float = Field(
        title = "tm",
        description = "Off-nominal tap ratio (p.u.) "
    )

    ta: float = Field(
        title = "ta",
        description = "Phase shifting angle (radian) "
    )


class DCLineInitialStatusBase(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
        description = "Connection status "
    )

    pdc_fr: float = Field(
        title = "pdc_fr",
        description = "Active power flow, from bus (p.u.) "
    )

    qdc_fr: float = Field(
        title = "qdc_fr",
        description = "Reactive power flow, from bus (p.u.) "
    )

    qdc_to: float = Field(
        title = "qdc_to",
        description = "Reactive power flow, to bus (p.u.) "
    )


