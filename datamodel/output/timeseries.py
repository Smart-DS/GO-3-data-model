import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel

class Bus(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Bus unique identifier "
    )

    # 

    vm: List[float] = Field(
        title = "vm",
        description = "Voltage magnitude (p.u.) "
    )

    va: List[float] = Field(
        title = "va",
        description = "Voltage angle (radian) "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 


class Shunt(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Shunt unique identifier "
    )

    on_status: List[bool] = Field(
        title = "on_status",
        description = "On-off status "
    )

    step: List[int] = Field(
        title = "step",
        description = "Number of step "
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

    on_status: List[bool] = Field(
        title = "on_status",
        description = "Connection status "
    )

    p: List[float] = Field(
        title = "p",
        description = "{ (Case: producer) Active production (p.u.) (Array of Float) }  { (Case: consumer) Active consumption (p.u.) "
    )

    q: List[float] = Field(
        title = "q",
        description = "{ (Case: producer) Reactive production (p.u.) (Array of Float)} { (Case: consumer) Reactive consumption (p.u.) "
    )

    p_reg_res_up: List[float] = Field(
        title = "p_reg_res_up",
        description = "Regulation up reserve (p.u.) "
    )

    p_reg_res_down: List[float] = Field(
        title = "p_reg_res_down",
        description = "Regulation down reserve (p.u.) "
    )

    p_syn_res: List[float] = Field(
        title = "p_syn_res",
        description = "Synchronized reserve (p.u.) "
    )

    p_nsyn_res: List[float] = Field(
        title = "p_nsyn_res",
        description = "Non-synchronized reserve (p.u.) "
    )

    p_ramp_res_up_online: List[float] = Field(
        title = "p_ramp_res_up_online",
        description = "Ramp up reserve when online (p.u.) "
    )

    p_ramp_res_down_online: List[float] = Field(
        title = "p_ramp_res_down_online",
        description = "Ramp down reserve when online (p.u.) "
    )

    p_ramp_res_up_offline: List[float] = Field(
        title = "p_ramp_res_up_offline",
        description = "Ramp up reserve when offline (p.u.) "
    )

    p_ramp_res_down_offline: List[float] = Field(
        title = "p_ramp_res_down_offline",
        description = "Ramp down reserve when offline (p.u.) "
    )

    q_res_up: List[float] = Field(
        title = "q_res_up",
        description = "Reactive reserve up (p.u.) "
    )

    q_res_down: List[float] = Field(
        title = "q_res_down",
        description = "Reactive reserve down (p.u.) "
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

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


class ACTransmissionLine(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "AC line unique identifier "
    )

    on_status: List[bool] = Field(
        title = "on_status",
        description = "Connection status "
    )

    # \end{tabular}

    # \end{center}


class TwoWindingTransformer(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Transformer line unique identifier "
    )

    tm: List[float] = Field(
        title = "tm",
        description = "Off-nominal taps ratio (p.u.) "
    )

    ta: List[float] = Field(
        title = "ta",
        description = "Phase shifting angle (radian) "
    )

    on_status: List[bool] = Field(
        title = "on_status",
        description = "Connection status "
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

    on_status: List[bool] = Field(
        title = "on_status",
        description = "Connection status "
    )

    pdc_fr: List[float] = Field(
        title = "pdc_fr",
        description = "Active power flow, from bus (p.u.) "
    )

    qdc_fr: List[float] = Field(
        title = "qdc_fr",
        description = "Reactive power flow, from bus (p.u.) "
    )

    qdc_to: List[float] = Field(
        title = "qdc_to",
        description = "Reactive power flow, to bus (p.u.) "
    )

    # \end{tabular}

    # \end{center}

    # 


