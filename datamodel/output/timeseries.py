import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union

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

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


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

    # \end{tabular}

    # \end{center}

    # 

    # 


class DispatchableDevices_SimpleProducingConsumingDevices(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Device unique identifier "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    p: float = Field(
        title = "p",
        description = "{ (Case: producer) Active production (Float, p.u.) }  { (Case: consumer) Active consumption "
    )

    q: float = Field(
        title = "q",
        description = "{ (Case: producer) Reactive production (Float, p.u.)} { (Case: consumer) Reactive consumption "
    )

    p_reg_res_up: float = Field(
        title = "p_reg_res_up",
        description = "Regulation up reserve "
    )

    p_reg_res_down: float = Field(
        title = "p_reg_res_down",
        description = "Regulation down reserve "
    )

    p_syn_res: float = Field(
        title = "p_syn_res",
        description = "Synchronized reserve "
    )

    p_nsyn_res: float = Field(
        title = "p_nsyn_res",
        description = "Non-synchronized reserve "
    )

    p_ramp_res_up_online: float = Field(
        title = "p_ramp_res_up_online",
        description = "Ramp up reserve when online "
    )

    p_ramp_res_down_online: float = Field(
        title = "p_ramp_res_down_online",
        description = "Ramp down reserve when online "
    )

    p_ramp_res_up_offline: float = Field(
        title = "p_ramp_res_up_offline",
        description = "Ramp up reserve when offline "
    )

    p_ramp_res_down_offline: float = Field(
        title = "p_ramp_res_down_offline",
        description = "Ramp down reserve when offline "
    )

    q_res_up: float = Field(
        title = "q_res_up",
        description = "Reactive reserve up "
    )

    q_res_down: float = Field(
        title = "q_res_down",
        description = "Reactive reserve down "
    )

    # \end{tabular}

    # \end{center}

    # 


class DispatchableDevices_MultimodeProducingConsumingDevices(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Device unique identifier "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    select_mode: str = Field(
        title = "select_mode",
        description = "Unique identifier of selected mode "
    )

    p: float = Field(
        title = "p",
        description = "{ (Case: producer) Active production (Float, p.u.) }  { (Case: consumer) Active consumption "
    )

    q: float = Field(
        title = "q",
        description = "{ (Case: producer) Reactive production (Float, p.u.)} { (Case: consumer) Reactive consumption "
    )

    p_reg_res_up: float = Field(
        title = "p_reg_res_up",
        description = "Regulation up reserve "
    )

    p_reg_res_down: float = Field(
        title = "p_reg_res_down",
        description = "Regulation down reserve "
    )

    p_syn_res: float = Field(
        title = "p_syn_res",
        description = "Synchronized reserve "
    )

    p_nsyn_res: float = Field(
        title = "p_nsyn_res",
        description = "Non-synchronized reserve "
    )

    p_ramp_res_up_online: float = Field(
        title = "p_ramp_res_up_online",
        description = "Ramp up reserve when online "
    )

    p_ramp_res_down_online: float = Field(
        title = "p_ramp_res_down_online",
        description = "Ramp down reserve when online "
    )

    p_ramp_res_up_offline: float = Field(
        title = "p_ramp_res_up_offline",
        description = "Ramp up reserve when offline "
    )

    p_ramp_res_down_offline: float = Field(
        title = "p_ramp_res_down_offline",
        description = "Ramp down reserve when offline "
    )

    q_res_up: float = Field(
        title = "q_res_up",
        description = "Reactive reserve up "
    )

    q_res_down: float = Field(
        title = "q_res_down",
        description = "Reactive reserve down "
    )

    # \end{tabular}

    # \end{center}

    # 


class SubdeviceUnitsforMultiModeProducingConsumingDevices(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Device unique identifier "
    )

    status: bool = Field(
        title = "status",
        description = "Connection status "
    )

    # \end{tabular}

    # \end{center}

    # 


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

    # \end{tabular}

    # \end{center}


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

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 

    # 

    # 


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

    # \end{tabular}

    # \end{center}

    # 


class RegionalReserves(BidDSJsonBaseModel):

    # Active reserve output attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REG_UP: float = Field(
        title = "REG_UP",
        description = "Regulation reserve up procurement "
    )

    REG_DOWN: float = Field(
        title = "REG_DOWN",
        description = "Regulation reserve down procurement "
    )

    SYN: float = Field(
        title = "SYN",
        description = "Synchronized reserve procurement"
    )

    NSYN: float = Field(
        title = "NSYN",
        description = "Non-synchronized reserve procurement"
    )

    RAMPING_RESERVE_UP: float = Field(
        title = "RAMPING_RESERVE_UP",
        description = "Ramping reserve up procurement "
    )

    RAMPING_RESERVE_DOWN: float = Field(
        title = "RAMPING_RESERVE_DOWN",
        description = "Ramping reserve down procurement "
    )

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reactive reserve output attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REACT_UP: float = Field(
        title = "REACT_UP",
        description = "Reactive reserve power up procurement "
    )

    REACT_DOWN: float = Field(
        title = "REACT_DOWN",
        description = "Reactive reserve power down procurement "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 


