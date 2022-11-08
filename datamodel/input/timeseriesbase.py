import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel

class GeneralBase(BidDSJsonBaseModel):

    # Global time attributes

    time_periods: StrictInt = Field(
        title = "time_periods",
        description = "The number of time periods "
    )

    interval_duration: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "interval_duration",
        description = "Time duration of the intervals, per time period in hours "
    )

    # Qualitative descriptors

    # Normalization attributes


class DispatchableDevices_SimpleProducingConsumingDevicesBase(BidDSJsonBaseModel):

    # Device attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    # 

    # Flags for extra parameters

    # Device attributes

    on_status_ub: List[conint(ge=0, le=1, strict=True)] = Field(
        title = "on_status_ub",
        description = "{On status indicator upper bound "
    )

    on_status_lb: List[conint(ge=0, le=1, strict=True)] = Field(
        title = "on_status_lb",
        description = "{On status indicator lower bound "
    )

    p_ub: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_ub",
        description = "{ (Case: producer) Upper bound of active dispatch in p.u. (Array of Float)   } { (Case: consumer) Upper bound of active demand in p.u.  "
    )

    p_lb: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_lb",
        description = "{ (Case: producer) Lower bound of active dispatch in p.u. (Array of Float)    } { (Case: consumer) Lower bound of active demand in p.u.  "
    )

    q_ub: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_ub",
        description = "{ (Case: producer) Upper bound of reactive dispatch in p.u.(Array of Float)  } { (Case: consumer) Upper bound of reactive demand  in p.u. "
    )

    q_lb: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_lb",
        description = "{ (Case: producer) Lower bound of reactive dispatch in p.u. (Array of Float)  } { (Case: consumer) Lower bound of reactive demand in p.u.  "
    )

    cost: List[List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]]] = Field(
        title = "cost",
        description = "A time series array of cost functions, where each function is represented as an array of cost block.  A cost block is an array (pair) with exactly two elements: 1) marginal cost in \$/p.u.-hr (Float), and 2) block size in p.u. (Float) "
    )

    # Reserve attributes

    # Time varying reserve attributes

    p_reg_res_up_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_reg_res_up_cost",
        description = "Costs for regulation reserve up in \$/pu-h  "
    )

    p_reg_res_down_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_reg_res_down_cost",
        description = "Costs for regulation reserve down in \$/pu-h "
    )

    p_syn_res_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_syn_res_cost",
        description = "Costs for synchronized reserve in \$/pu-h  "
    )

    p_nsyn_res_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_nsyn_res_cost",
        description = "Costs for non-synchronized reserve in \$/pu-h  "
    )

    p_ramp_res_up_online_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_ramp_res_up_online_cost",
        description = "Costs for ramp up reserve when online in \$/pu-h  "
    )

    p_ramp_res_down_online_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_ramp_res_down_online_cost",
        description = "Costs for ramp down reserve when online in \$/pu-h  "
    )

    p_ramp_res_up_offline_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_ramp_res_up_offline_cost",
        description = "Costs for ramp up reserve when offline in \$/pu-h  "
    )

    p_ramp_res_down_offline_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "p_ramp_res_down_offline_cost",
        description = "Costs for ramp down reserve when offline in \$/pu-h  "
    )

    q_res_up_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_res_up_cost",
        description = "Costs for reactive reserve up in \$/pu-h "
    )

    q_res_down_cost: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_res_down_cost",
        description = "Costs for reactive reserve down in \$/pu-h "
    )

    # 


class ActiveZonalReserveRequirementsViolationCostsBase(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Zone reserve unique identifier "
    )

    RAMPING_RESERVE_UP: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "RAMPING_RESERVE_UP",
        description = "Ramping reserve up requirement "
    )

    RAMPING_RESERVE_DOWN: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "RAMPING_RESERVE_DOWN",
        description = "Ramping reserve down requirement "
    )


class ReactiveZonalReserveRequirementsViolationCostsBase(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REACT_UP: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "REACT_UP",
        description = "Reactive reserve power up requirement "
    )

    REACT_DOWN: List[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "REACT_DOWN",
        description = "Reactive reserve power down requirement "
    )


