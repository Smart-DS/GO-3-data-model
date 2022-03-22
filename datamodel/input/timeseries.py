import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union

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

    # \end{tabular}

    # \end{center}

    # 


class DispatchableDevices_SimpleProducingConsumingDevices_initial_status(BidDSJsonBaseModel):

    on_status: int = Field(
        title = "on_status",
        description = "On status indicator for initial time step ",
        options = [0, 1]
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
class DispatchableDevices_SimpleProducingConsumingDevices(BidDSJsonBaseModel):

    # Device attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    on_status_ub: int = Field(
        title = "on_status_ub",
        description = "On status indicator upper bound ",
        options = [0, 1]
    )

    on_status_lb: int = Field(
        title = "on_status_lb",
        description = "On status indicator lower bound ",
        options = [0, 1]
    )

    # 

    p_ub: float = Field(
        title = "p_ub",
        description = "{ (Case: producer) Upper bound of active dispatch (Float, p.u.)   } { (Case: consumer) Upper bound of active demand   "
    )

    p_lb: float = Field(
        title = "p_lb",
        description = "{ (Case: producer) Lower bound of active dispatch (Float, p.u.)   } { (Case: consumer) Lower bound of active demand   "
    )

    q_ub: float = Field(
        title = "q_ub",
        description = "{ (Case: producer) Upper bound of reactive dispatch (Float, p.u.) } { (Case: consumer) Upper bound of reactive demand   "
    )

    q_lb: float = Field(
        title = "q_lb",
        description = "{ (Case: producer) Lower bound of reactive dispatch (Float, p.u.) } { (Case: consumer) Lower bound of reactive demand   "
    )

    # 

    cost: float = Field(
        title = "cost",
        description = "Array of cost blocks, where   each cost block is an array with exactly two elements:     1) marginal  cost (\$/p.u.-hr), and 2) block size "
    )

    # 

    # Flags for extra parameters

    # \end{tabular}

    # \end{center}

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reserve attributes

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Initial condition attributes

    # Reactive cap. attributes

    # Reactive cap. attributes

    # 

    # \end{tabular}

    # \end{center}

    # 

    # 

    # \begin{todo}[]{}

    # Output solution --- a preliminary version with state/configuration is drafted.

    # \end{todo}

    # 


class DispatchableDevices_MultimodeProducingConsumingDevices_initial_status(BidDSJsonBaseModel):

    on_status: int = Field(
        title = "on_status",
        description = "On status indicator for initial time step ",
        options = [0, 1]
    )

    select_mode: str = Field(
        title = "select_mode",
        description = "Active mode uid for initial time step "
    )

    p: float = Field(
        title = "p",
        description = "{ (Case: producer) Active production for initial time step (Float, p.u.) } { (Case: consumer) Active consumption for initial time step "
    )

    q: float = Field(
        title = "q",
        description = "{ (Case: producer) Reactive production for initial time step (Float, p.u.) } { (Case: consumer) Reactive consumption for initial time step "
    )
class DispatchableDevices_MultimodeProducingConsumingDevices_modes(BidDSJsonBaseModel):

    uid: str = Field(
        title = "uid",
        description = "Mode unique identifier "
    )

    description: Optional[str] = Field(
        title = "description",
        description = "Mode description "
    )

    select_ub: int = Field(
        title = "select_ub",
        description = "Mode selection upper bound ",
        options = [0, 1]
    )

    select_lb: int = Field(
        title = "select_lb",
        description = "Mode selection lower bound ",
        options = [0, 1]
    )

    mode_transition_uids: List[str] = Field(
        title = "mode_transition_uids",
        description = "Array of feasible mode uids to transit to "
    )

    on_subdevice_uids: List[str] = Field(
        title = "on_subdevice_uids",
        description = "Array of associated subdevice uids that must be   online for current mode "
    )

    p_ub: float = Field(
        title = "p_ub",
        description = "{ (Case: producer) Upper bound of active dispatch (Float, p.u.)   } { (Case: consumer) Upper bound of active demand   "
    )

    p_lb: float = Field(
        title = "p_lb",
        description = "{ (Case: producer) Lower bound of active dispatch (Float, p.u.)   } { (Case: consumer) Lower bound of active demand   "
    )

    q_ub: float = Field(
        title = "q_ub",
        description = "{ (Case: producer) Upper bound of reactive dispatch (Float, p.u.) } { (Case: consumer) Upper bound of reactive demand   "
    )

    q_lb: float = Field(
        title = "q_lb",
        description = "{ (Case: producer) Lower bound of reactive dispatch (Float, p.u.) } { (Case: consumer) Lower bound of reactive demand   "
    )

    cost: float = Field(
        title = "cost",
        description = "Array of cost blocks, where   each block is an array with exactly two elements:     a) marginal cost (\$/p.u.-hr), and b) block size "
    )

    on_cost: float = Field(
        title = "on_cost",
        description = "Mode fixed operating cost "
    )

    mode_transit_cost: float = Field(
        title = "mode_transit_cost",
        description = "An inner JSON object for describing transition cost from each operating   mode. (JSON keys: mode uids, JSON value: transition cost "
    )

    p_ramp_up_ub: float = Field(
        title = "p_ramp_up_ub",
        description = "{(Case: producer) Max production ramp up when operating (Float, p.u./hr)}  {(Case: consumer) Max consumption ramp up when operating "
    )

    p_ramp_down_ub: float = Field(
        title = "p_ramp_down_ub",
        description = "{(Case: producer) Max production ramp down when operating (Float, pu/hr)}  {(Case: consumer) Max consumption ramp down when operating "
    )

    dwell_time_ub: float = Field(
        title = "dwell_time_ub",
        description = "Maximum dwell time "
    )

    dwell_time_lb: float = Field(
        title = "dwell_time_lb",
        description = "Minimum dwell time "
    )

    initial_status: DispatchableDevices_MultimodeProducingConsumingDevices_initial_status = Field(
        title = "initial_status",
        description = "A JSON object storing data for the initial time step "
    )
class DispatchableDevices_MultimodeProducingConsumingDevices_modes(BidDSJsonBaseModel):

    p_reg_res_up_ub: float = Field(
        title = "p_reg_res_up_ub",
        description = "Maximum regulation reserve up "
    )

    p_reg_res_down_ub: float = Field(
        title = "p_reg_res_down_ub",
        description = "Maximum regulation reserve down "
    )

    p_syn_res_ub: float = Field(
        title = "p_syn_res_ub",
        description = "Maximum synchronized reserve "
    )

    p_nsyn_res_ub: float = Field(
        title = "p_nsyn_res_ub",
        description = "Maximum non-synchronized reserve "
    )

    p_ramp_res_up_online_ub: float = Field(
        title = "p_ramp_res_up_online_ub",
        description = "Maximum ramp up reserve when online "
    )

    p_ramp_res_down_online_ub: float = Field(
        title = "p_ramp_res_down_online_ub",
        description = "Maximum ramp down reserve when online "
    )

    p_ramp_res_up_offline_ub: float = Field(
        title = "p_ramp_res_up_offline_ub",
        description = "Maximum ramp up reserve when offline "
    )

    p_ramp_res_down_offline_ub: float = Field(
        title = "p_ramp_res_down_offline_ub",
        description = "Maximum ramp down reserve when offline "
    )
class DispatchableDevices_MultimodeProducingConsumingDevices_initial_status(BidDSJsonBaseModel):

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time for current mode "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time for current mode "
    )
class DispatchableDevices_MultimodeProducingConsumingDevices(BidDSJsonBaseModel):

    # Operations attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    on_status_ub: int = Field(
        title = "on_status_ub",
        description = "On status indicator upper bound ",
        options = [0, 1]
    )

    on_status_lb: int = Field(
        title = "on_status_lb",
        description = "On status indicator lower bound ",
        options = [0, 1]
    )

    # 

    # 

    modes: List[DispatchableDevices_MultimodeProducingConsumingDevices_modes] = Field(
        title = "modes",
        description = "An array of mode JSON objects "
    )

    # Flags for extra parameters

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Initial condition attributes

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Mode attributes

    uid: str = Field(
        title = "uid",
        description = "Mode unique identifier "
    )

    select_ub: int = Field(
        title = "select_ub",
        description = "Mode selection upper bound ",
        options = [0, 1]
    )

    select_lb: int = Field(
        title = "select_lb",
        description = "Mode selection lower bound ",
        options = [0, 1]
    )

    p_ub: float = Field(
        title = "p_ub",
        description = "{ (Case: producer) Upper bound of active dispatch (Float, p.u.)   } { (Case: consumer) Upper bound of active demand   "
    )

    p_lb: float = Field(
        title = "p_lb",
        description = "{ (Case: producer) Lower bound of active dispatch (Float, p.u.)   } { (Case: consumer) Lower bound of active demand   "
    )

    q_ub: float = Field(
        title = "q_ub",
        description = "{ (Case: producer) Upper bound of reactive dispatch (Float, p.u.) } { (Case: consumer) Upper bound of reactive demand   "
    )

    q_lb: float = Field(
        title = "q_lb",
        description = "{ (Case: producer) Lower bound of reactive dispatch (Float, p.u.) } { (Case: consumer) Lower bound of reactive demand   "
    )

    cost: float = Field(
        title = "cost",
        description = "Array of cost blocks, where   each block is an array with exactly two elements:     a) marginal cost (\$/p.u.-hr), and b) block size "
    )

    # \end{tabular}

    # \end{center}

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reserve attributes

    # Initial condition attributes

    # 

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reactive cap. attributes

    # \hline \hline

    # Reactive cap.

    # \end{tabular}

    # \end{center}

    # 


class SubdeviceUnitsforMultiModeProducingConsumingDevices_initial_status(BidDSJsonBaseModel):

    on_status: int = Field(
        title = "on_status",
        description = "On status indicator for initial time step ",
        options = [0, 1]
    )

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time "
    )
class SubdeviceUnitsforMultiModeProducingConsumingDevices(BidDSJsonBaseModel):

    # Sub-device attributes

    uid: str = Field(
        title = "uid",
        description = "Sub-device unique identifier "
    )

    on_status_ub: int = Field(
        title = "on_status_ub",
        description = "On status indicator upper bound ",
        options = [0, 1]
    )

    on_status_lb: int = Field(
        title = "on_status_lb",
        description = "On status indicator lower bound ",
        options = [0, 1]
    )

    # 

    # 

    # \end{tabular}

    # }

    # \end{center}

    # 

    # \begin{center}

    # \small

    # {\color{red}

    # \begin{tabular}{ l | l | c | c | c |}

    # Initial condition attributes

    # \end{tabular}

    # }

    # \end{center}

    # 


class RegionalReserves(BidDSJsonBaseModel):

    # Active reserve attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REG_UP: float = Field(
        title = "REG_UP",
        description = "Regulation reserve up requirement "
    )

    REG_DOWN: float = Field(
        title = "REG_DOWN",
        description = "Regulation reserve down requirement "
    )

    SYN: float = Field(
        title = "SYN",
        description = "Synchronized reserve requirement "
    )

    NSYN: float = Field(
        title = "NSYN",
        description = "Non-synchronized reserve requirement "
    )

    RAMPING_RESERVE_UP: float = Field(
        title = "RAMPING_RESERVE_UP",
        description = "Ramping reserve up requirement "
    )

    RAMPING_RESERVE_DOWN: float = Field(
        title = "RAMPING_RESERVE_DOWN",
        description = "Ramping reserve down requirement "
    )

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reactive reserve attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REACT_UP: float = Field(
        title = "REACT_UP",
        description = "Reactive reserve power up requirement "
    )

    REACT_DOWN: float = Field(
        title = "REACT_DOWN",
        description = "Reactive reserve power down requirement "
    )

    # \end{tabular}

    # \end{center}

    # 


