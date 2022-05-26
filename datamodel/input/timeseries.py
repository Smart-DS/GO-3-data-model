import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel

class General(BidDSJsonBaseModel):

    # Global time attributes

    time_periods: int = Field(
        title = "time_periods",
        description = "The number of time periods "
    )

    interval_duration: List[float] = Field(
        title = "interval_duration",
        description = "Time duration of the intervals, per time period in hours  "
    )

    # Qualitative descriptors

    # Normalization attributes


class DispatchableDevices_SimpleProducingConsumingDevices(BidDSJsonBaseModel):

    # Device attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    # 

    # Flags for extra parameters

    on_status_ub: List[bool] = Field(
        title = "on_status_ub",
        description = "{On status indicator upper bound "
    )

    on_status_lb: List[bool] = Field(
        title = "on_status_lb",
        description = "{On status indicator lower bound "
    )

    p_ub: List[float] = Field(
        title = "p_ub",
        description = "{ (Case: producer) Upper bound of active dispatch (Array of Float)   } { (Case: consumer) Upper bound of active demand   "
    )

    p_lb: List[float] = Field(
        title = "p_lb",
        description = "{ (Case: producer) Lower bound of active dispatch (Array of Float)    } { (Case: consumer) Lower bound of active demand   "
    )

    q_ub: List[float] = Field(
        title = "q_ub",
        description = "{ (Case: producer) Upper bound of reactive dispatch (Array of Float)  } { (Case: consumer) Upper bound of reactive demand   "
    )

    q_lb: List[float] = Field(
        title = "q_lb",
        description = "{ (Case: producer) Lower bound of reactive dispatch (Array of Float)  } { (Case: consumer) Lower bound of reactive demand   "
    )

    # 

    cost: List[List[Tuple[float,float]]] = Field(
        title = "cost",
        description = "Array of cost blocks, where   each cost block is an array with exactly two elements:     1) marginal  cost (\$/p.u.-hr), and 2) block size (p.u.) "
    )

    # Time varying reserve attributes

    p_reg_res_up_cost: List[float] = Field(
        title = "p_reg_res_up_cost",
        description = "Costs for regulation reserve up (\$/pu-h)  "
    )

    p_reg_res_down_cost: List[float] = Field(
        title = "p_reg_res_down_cost",
        description = "Costs for regulation reserve down (\$/pu-h) "
    )

    p_syn_res_cost: List[float] = Field(
        title = "p_syn_res_cost",
        description = "Costs for synchronized reserve (\$/pu-h)  "
    )

    p_nsyn_res_cost: List[float] = Field(
        title = "p_nsyn_res_cost",
        description = "Costs for non-synchronized reserve (\$/pu-h)  "
    )

    p_ramp_res_up_online_cost: List[float] = Field(
        title = "p_ramp_res_up_online_cost",
        description = "Costs for ramp up reserve when online (\$/pu-h)  "
    )

    p_ramp_res_down_online_cost: List[float] = Field(
        title = "p_ramp_res_down_online_cost",
        description = "Costs for ramp down reserve when online (\$/pu-h)  "
    )

    p_ramp_res_up_offline_cost: List[float] = Field(
        title = "p_ramp_res_up_offline_cost",
        description = "Costs for ramp up reserve when offline (\$/pu-h)  "
    )

    p_ramp_res_down_offline_cost: List[float] = Field(
        title = "p_ramp_res_down_offline_cost",
        description = "Costs for ramp down reserve when offline (\$/pu-h)  "
    )

    q_res_up_cost: List[float] = Field(
        title = "q_res_up_cost",
        description = "Costs for reactive reserve up (\$/pu-h) "
    )

    q_res_down_cost: List[float] = Field(
        title = "q_res_down_cost",
        description = "Costs for reactive reserve down (\$/pu-h) "
    )

    # 


class ActiveZonalReserveRequirementsViolationCosts(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Zone reserve unique identifier "
    )

    RAMPING_RESERVE_UP: List[float] = Field(
        title = "RAMPING_RESERVE_UP",
        description = "Ramping reserve up requirement "
    )

    RAMPING_RESERVE_DOWN: List[float] = Field(
        title = "RAMPING_RESERVE_DOWN",
        description = "Ramping reserve down requirement "
    )


class ReactiveZonalReserveRequirementsViolationCosts(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REACT_UP: List[float] = Field(
        title = "REACT_UP",
        description = "Reactive reserve power up requirement "
    )

    REACT_DOWN: List[float] = Field(
        title = "REACT_DOWN",
        description = "Reactive reserve power down requirement "
    )


