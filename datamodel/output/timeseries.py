import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import String, Dict, List, Optional, Union

from datamodel.base import BidDSJsonBaseModel

class Bus(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Bus unique identifier "
    )

    vm: float = Field(
        title = "vm",
        description = "Voltage magnitude "
    )

    va: Optional[float] = Field(
        title = "va",
        description = "Voltage angle "
    )


class Shunt(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Shunt unique identifier "
    )

    steps: int = Field(
        title = "steps",
        description = "Number of steps "
    )


class ProducingDevices_MultipleModeGeneratingUnits(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Dispatchable device unique identifier "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    select_config: List[str] = Field(
        title = "select_config",
        description = "Active configuration uids for each time step "
    )

    pg: float = Field(
        title = "pg",
        description = "Active dispatch "
    )

    qg: float = Field(
        title = "qg",
        description = "Reactive dispatch "
    )

    pg_regulation_down: float = Field(
        title = "pg_regulation_down",
        description = "Regulation down reserve "
    )

    pg_regulation_up: float = Field(
        title = "pg_regulation_up",
        description = "Regulation up reserve "
    )

    pg_spin: float = Field(
        title = "pg_spin",
        description = "Spinning reserve "
    )

    pg_cont: float = Field(
        title = "pg_cont",
        description = "Contingency reserve "
    )

    energy: float = Field(
        title = "energy",
        description = "Energy storage "
    )


class ACTransmissionLine(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "AC line unique identifier "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    # Optional output attributes

    pl_fr: Optional[float] = Field(
        title = "pl_fr",
        description = "Active power flow, from side "
    )

    ql_fr: Optional[float] = Field(
        title = "ql_fr",
        description = "Reactive power flow, from side "
    )

    pl_to: Optional[float] = Field(
        title = "pl_to",
        description = "Active power flow, to side "
    )

    ql_to: Optional[float] = Field(
        title = "ql_to",
        description = "Reactive power flow, to side "
    )


class TwoWindingTransformer(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Transformer line unique identifier "
    )

    tm: float = Field(
        title = "tm",
        description = "Off-nominal taps ratio "
    )

    ta: float = Field(
        title = "ta",
        description = "Phase shifting angle "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    # Optional output attributes

    pl_fr: Optional[float] = Field(
        title = "pl_fr",
        description = "Active power flow, from side "
    )

    ql_fr: Optional[float] = Field(
        title = "ql_fr",
        description = "Reactive power flow, from side "
    )

    pl_to: Optional[float] = Field(
        title = "pl_to",
        description = "Active power flow, to side "
    )

    ql_to: Optional[float] = Field(
        title = "ql_to",
        description = "Reactive power flow, to side "
    )


class DCLine(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "DC line unique identifier "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    pdc_fr: float = Field(
        title = "pdc_fr",
        description = "Active power flow, from bus "
    )

    qdc_fr: float = Field(
        title = "qdc_fr",
        description = "Reactive power flow, from bus "
    )

    qdc_to: float = Field(
        title = "qdc_to",
        description = "Reactive power flow, to bus "
    )


