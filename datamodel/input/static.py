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

    # 

    # Normalization attributes

    base_norm_mva: Optional[float] = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
    )

    # \end{tabular}

    # \end{center}

    # 


class ViolationCostsParameters(BidDSJsonBaseModel):

    # Global violation attributes

    p_bus_vio_cost: float = Field(
        title = "p_bus_vio_cost",
        description = "Bus violation costs for active power violation "
    )

    q_bus_vio_cost: float = Field(
        title = "q_bus_vio_cost",
        description = "Bus violation costs for reactive power violation  "
    )

    s_vio_cost: float = Field(
        title = "s_vio_cost",
        description = "Branch violation costs for thermal violation "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 


class Bus(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Bus unique identifier "
    )

    vm_ub: float = Field(
        title = "vm_ub",
        description = "Voltage magnitude upper bound "
    )

    vm_lb: float = Field(
        title = "vm_lb",
        description = "Voltage magnitude lower bound "
    )

    con_loss_factor: float = Field(
        title = "con_loss_factor",
        description = "Contingency participation loss factor "
    )

    active_reserve_uids: List[str] = Field(
        title = "active_reserve_uids",
        description = "List of active reserve zones "
    )

    # 

    reactive_reserve_uids: List[str] = Field(
        title = "reactive_reserve_uids",
        description = "List of reactive reserve zones "
    )

    # 

    # Operations information

    base_nom_volt: Optional[float] = Field(
        title = "base_nom_volt",
        description = "Bus nominal voltage "
    )

    type: Optional[str] = Field(
        title = "type",
        description = "Bus type ",
        options = ["PQ"]
    )

    # Location information

    area: Optional[str] = Field(
        title = "area",
        description = "Bus control area "
    )

    zone: Optional[str] = Field(
        title = "zone",
        description = "Bus control zone "
    )

    longitude: Optional[float] = Field(
        title = "longitude",
        description = "Bus location - longitude "
    )

    latitude: Optional[float] = Field(
        title = "latitude",
        description = "Bus location - latitude "
    )

    city: Optional[str] = Field(
        title = "city",
        description = "Bus city location "
    )

    county: Optional[str] = Field(
        title = "county",
        description = "Bus county location "
    )

    state: Optional[str] = Field(
        title = "state",
        description = "Bus state location "
    )

    country: Optional[str] = Field(
        title = "country",
        description = "Bus country location "
    )

    # \end{tabular}

    # \end{center}


class Shunt(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Shunt unique identifier "
    )

    bus: str = Field(
        title = "bus",
        description = "Unique identifier for connecting bus "
    )

    gs: float = Field(
        title = "gs",
        description = "Shunt conductance for one step "
    )

    bs: float = Field(
        title = "bs",
        description = "Shunt susceptance for one step "
    )

    steps_ub: int = Field(
        title = "steps_ub",
        description = "Maximum number of steps "
    )

    steps_lb: int = Field(
        title = "steps_lb",
        description = "Minimum number of steps "
    )

    # \end{tabular}

    # \end{center}

    # 


class DispatchableDevices_SimpleProducingConsumingDevices(BidDSJsonBaseModel):

    # Device attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    bus: str = Field(
        title = "bus",
        description = "Unique identifier for connecting bus "
    )

    device_type: str = Field(
        title = "device_type",
        description = "Type of device ",
        options = ["producer / consumer"]
    )

    vm_setpoint: Optional[float] = Field(
        title = "vm_setpoint",
        description = "Voltage magnitude setpoint "
    )

    startup_cost: float = Field(
        title = "startup_cost",
        description = "Device start up cost "
    )

    shutdown_cost: float = Field(
        title = "shutdown_cost",
        description = "Device shut down cost "
    )

    # 

    startup_num_ub: int = Field(
        title = "startup_num_ub",
        description = "Maximum startups "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    on_cost: float = Field(
        title = "on_cost",
        description = "Device fixed operating cost "
    )

    in_service_time_lb: float = Field(
        title = "in_service_time_lb",
        description = "Minimum uptime in service "
    )

    down_time_lb: float = Field(
        title = "down_time_lb",
        description = "Minimum downtime "
    )

    p_ramp_up_ub: float = Field(
        title = "p_ramp_up_ub",
        description = "{\color{red}(Case: producer) Max production ramp up when operating "
    )

    # 

    p_ramp_down_ub: float = Field(
        title = "p_ramp_down_ub",
        description = "{\color{red}(Case: producer) Max production ramp down when operating "
    )

    # 

    p_startup_ramp_ub: float = Field(
        title = "p_startup_ramp_ub",
        description = "{\color{red}(Case: producer) Max production ramp up when start up "
    )

    # 

    p_shutdown_ramp_ub: float = Field(
        title = "p_shutdown_ramp_ub",
        description = "{\color{red}(Case: producer) Max production ramp down when shut down "
    )

    # 

    # 

    # Flags for extra parameters

    q_linear_cap: bool = Field(
        title = "q_linear_cap",
        description = "Device has additional reactive constraint "
    )

    q_bound_cap: bool = Field(
        title = "q_bound_cap",
        description = "Device has additional reactive bounds "
    )

    storage_cap: bool = Field(
        title = "storage_cap",
        description = "Device has storage capability "
    )

    # \end{tabular}

    # \end{center}

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reserve attributes

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

    q_res_up_ub: float = Field(
        title = "q_res_up_ub",
        description = "Maximum reactive reserve up "
    )

    q_res_down_ub: float = Field(
        title = "q_res_down_ub",
        description = "Maximum reactive reserve down "
    )

    p_reg_res_up_cost: float = Field(
        title = "p_reg_res_up_cost",
        description = "Costs for regulation reserve up "
    )

    p_reg_res_down_cost: float = Field(
        title = "p_reg_res_down_cost",
        description = "Costs for regulation reserve down "
    )

    p_syn_res_cost: float = Field(
        title = "p_syn_res_cost",
        description = "Costs for synchronized reserve "
    )

    p_nsyn_res_cost: float = Field(
        title = "p_nsyn_res_cost",
        description = "Costs for non-synchronized reserve "
    )

    p_ramp_res_up_online_cost: float = Field(
        title = "p_ramp_res_up_online_cost",
        description = "Costs for ramp up reserve when online "
    )

    p_ramp_res_down_online_cost: float = Field(
        title = "p_ramp_res_down_online_cost",
        description = "Costs for ramp down reserve when online "
    )

    p_ramp_res_up_offline_cost: float = Field(
        title = "p_ramp_res_up_offline_cost",
        description = "Costs for ramp up reserve when offline "
    )

    p_ramp_res_down_offline_cost: float = Field(
        title = "p_ramp_res_down_offline_cost",
        description = "Costs for ramp down reserve when offline "
    )

    q_res_up_cost: float = Field(
        title = "q_res_up_cost",
        description = "Costs for reactive reserve up "
    )

    q_res_down_cost: float = Field(
        title = "q_res_down_cost",
        description = "Costs for reactive reserve down "
    )

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Initial condition attributes

    on_status: int = Field(
        title = "on_status",
        description = "On status indicator for initial time step ",
        options = [0, 1]
    )

    p: float = Field(
        title = "p",
        description = "{\color{red} (Case: producer) Active production for initial time step "
    )

    # 

    q: float = Field(
        title = "q",
        description = "{\color{red} (Case: producer) Reactive production for initial time step "
    )

    # 

    energy: float = Field(
        title = "energy",
        description = "Energy storage for initial time step "
    )

    # 

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time "
    )

    # Reactive cap. attributes

    q_0: float = Field(
        title = "q_0",
        description = "{\color{red} (Case: producer) Reactive production at zero active production "
    )

    # 

    pq_ratio: float = Field(
        title = "pq_ratio",
        description = "Sensitivity of reactive w.r.t active dispatch "
    )

    # Reactive cap. attributes

    q_0_ub: float = Field(
        title = "q_0_ub",
        description = "{\color{red} (Case: producer) Max reactive production at zero active production "
    )

    # 

    q_0_lb: float = Field(
        title = "q_0_lb",
        description = "{\color{red} (Case: producer) Min reactive production at zero active production "
    )

    # 

    # 

    pq_ratio_ub: float = Field(
        title = "pq_ratio_ub",
        description = "Upper bound for sensitivity of reactive w.r.t active dispatch "
    )

    pq_ratio_lb: float = Field(
        title = "pq_ratio_lb",
        description = "Lower bound for sensitivity of reactive w.r.t active dispatch "
    )

    # Storage attributes

    storage_efficiency: float = Field(
        title = "storage_efficiency",
        description = "Efficiency of storage device "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # \begin{todo}[]{}

    # Output solution --- a preliminary version with state/configuration is drafted.

    # \end{todo}

    # 


class DispatchableDevices_MultimodeProducingConsumingDevices(BidDSJsonBaseModel):

    # Operations attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    bus: str = Field(
        title = "bus",
        description = "Unique identifier for connecting bus "
    )

    device_type: str = Field(
        title = "device_type",
        description = "Type of device ",
        options = ["producer / consumer"]
    )

    vm_setpoint: Optional[float] = Field(
        title = "vm_setpoint",
        description = "Voltage magnitude setpoint "
    )

    startup_cost: float = Field(
        title = "startup_cost",
        description = "Device start up cost "
    )

    shutdown_cost: float = Field(
        title = "shutdown_cost",
        description = "Device shut down cost "
    )

    startup_num_ub: int = Field(
        title = "startup_num_ub",
        description = "Maximum startups "
    )

    in_service_time_lb: float = Field(
        title = "in_service_time_lb",
        description = "Minimum uptime in service "
    )

    down_time_lb: float = Field(
        title = "down_time_lb",
        description = "Minimum downtime "
    )

    p_startup_ramp_ub: float = Field(
        title = "p_startup_ramp_ub",
        description = "{\color{red}(Case: producer) Max production ramp up when start up "
    )

    # 

    p_shutdown_ramp_ub: float = Field(
        title = "p_shutdown_ramp_ub",
        description = "{\color{red}(Case: producer) Max production ramp down when shut down "
    )

    # 

    # 

    # 

    mode_num: Optional[int] = Field(
        title = "mode_num",
        description = "Number of operating modes "
    )

    # Flags for extra parameters

    q_linear_cap: bool = Field(
        title = "q_linear_cap",
        description = "Device has additional reactive constraint "
    )

    q_bound_cap: bool = Field(
        title = "q_bound_cap",
        description = "Device has additional reactive bounds "
    )

    storage_cap: bool = Field(
        title = "storage_cap",
        description = "Device has storage capability "
    )

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Initial condition attributes

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
        description = "{\color{red} (Case: producer) Active production for initial time step "
    )

    # 

    q: float = Field(
        title = "q",
        description = "{\color{red} (Case: producer) Reactive production for initial time step "
    )

    # 

    energy: float = Field(
        title = "energy",
        description = "Energy storage for initial time step "
    )

    # 

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

    description: Optional[str] = Field(
        title = "description",
        description = "Mode description "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    on_cost: float = Field(
        title = "on_cost",
        description = "Mode fixed operating cost "
    )

    # 

    p_ramp_up_ub: float = Field(
        title = "p_ramp_up_ub",
        description = "{\color{red}(Case: producer) Max production ramp up when operating "
    )

    # 

    p_ramp_down_ub: float = Field(
        title = "p_ramp_down_ub",
        description = "{\color{red}(Case: producer) Max production ramp down when operating "
    )

    # 

    # \end{tabular}

    # \end{center}

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reserve attributes

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

    q_res_up_ub: float = Field(
        title = "q_res_up_ub",
        description = "Maximum reactive reserve up "
    )

    q_res_down_ub: float = Field(
        title = "q_res_down_ub",
        description = "Maximum reactive reserve down "
    )

    p_reg_res_up_cost: float = Field(
        title = "p_reg_res_up_cost",
        description = "Costs for regulation reserve up "
    )

    p_reg_res_down_cost: float = Field(
        title = "p_reg_res_down_cost",
        description = "Costs for regulation reserve down "
    )

    p_syn_res_cost: float = Field(
        title = "p_syn_res_cost",
        description = "Costs for synchronized reserve "
    )

    p_nsyn_res_cost: float = Field(
        title = "p_nsyn_res_cost",
        description = "Costs for non-synchronized reserve "
    )

    p_ramp_res_up_online_cost: float = Field(
        title = "p_ramp_res_up_online_cost",
        description = "Costs for ramp up reserve when online "
    )

    p_ramp_res_down_online_cost: float = Field(
        title = "p_ramp_res_down_online_cost",
        description = "Costs for ramp down reserve when online "
    )

    p_ramp_res_up_offline_cost: float = Field(
        title = "p_ramp_res_up_offline_cost",
        description = "Costs for ramp up reserve when offline "
    )

    p_ramp_res_down_offline_cost: float = Field(
        title = "p_ramp_res_down_offline_cost",
        description = "Costs for ramp down reserve when offline "
    )

    q_res_up_cost: float = Field(
        title = "q_res_up_cost",
        description = "Costs for reactive reserve up "
    )

    q_res_down_cost: float = Field(
        title = "q_res_down_cost",
        description = "Costs for reactive reserve down "
    )

    # Initial condition attributes

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time for current mode "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time for current mode "
    )

    # 

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reactive cap. attributes

    q_0: float = Field(
        title = "q_0",
        description = "{\color{red} (Case: producer) Reactive production at zero active production "
    )

    # 

    pq_ratio: float = Field(
        title = "pq_ratio",
        description = "Sensitivity of reactive w.r.t active dispatch "
    )

    # \hline \hline

    # Reactive cap.

    q_0_ub: float = Field(
        title = "q_0_ub",
        description = "{\color{red} (Case: producer) Max reactive production at zero active production "
    )

    # 

    q_0_lb: float = Field(
        title = "q_0_lb",
        description = "{\color{red} (Case: producer) Min reactive production at zero active production "
    )

    # 

    pq_ratio_ub: float = Field(
        title = "pq_ratio_ub",
        description = "Upper bound for sensitivity of reactive w.r.t active dispatch "
    )

    pq_ratio_lb: float = Field(
        title = "pq_ratio_lb",
        description = "Lower bound for sensitivity of reactive w.r.t active dispatch "
    )

    # Storage attributes

    storage_efficiency: float = Field(
        title = "storage_efficiency",
        description = "Efficiency of storage device "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 


class ACTransmissionLine(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "AC line unique identifier "
    )

    fr_bus: str = Field(
        title = "fr_bus",
        description = "Unique identifier for connecting from bus "
    )

    to_bus: str = Field(
        title = "to_bus",
        description = "Unique identifier for connecting to bus "
    )

    r: float = Field(
        title = "r",
        description = "Series resistance "
    )

    x: float = Field(
        title = "x",
        description = "Series reactance  "
    )

    b: float = Field(
        title = "b",
        description = "Shunt susceptance "
    )

    mva_ub_nom: float = Field(
        title = "mva_ub_nom",
        description = "MVA limit, nominal rating "
    )

    mva_ub_sht: Optional[float] = Field(
        title = "mva_ub_sht",
        description = "MVA limit, short term rating "
    )

    mva_ub_em: float = Field(
        title = "mva_ub_em",
        description = "MVA limit, emergency rating "
    )

    standby_cost: float = Field(
        title = "standby_cost",
        description = "Line fixed standby cost "
    )

    connection_cost: float = Field(
        title = "connection_cost",
        description = "AC Line connection cost "
    )

    disconnection_cost: float = Field(
        title = "disconnection_cost",
        description = "AC line disconnection cost "
    )

    additional_shunt: bool = Field(
        title = "additional_shunt",
        description = "Branch has additional shunt components "
    )

    # Additional shunt attributes

    g_fr: float = Field(
        title = "g_fr",
        description = "Conductance for shunt component at from bus "
    )

    b_fr: float = Field(
        title = "b_fr",
        description = "Susceptance for shunt component at from bus "
    )

    g_to: float = Field(
        title = "g_to",
        description = "Conductance for shunt component at to bus "
    )

    b_to: float = Field(
        title = "b_to",
        description = "Susceptance for shunt component at to bus "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 


class TwoWindingTransformer(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Transformer unique identifier "
    )

    fr_bus: str = Field(
        title = "fr_bus",
        description = "Unique identifier for connecting from/tap bus "
    )

    to_bus: str = Field(
        title = "to_bus",
        description = "Unique identifier for connecting to bus "
    )

    r: float = Field(
        title = "r",
        description = "Series resistance "
    )

    x: float = Field(
        title = "x",
        description = "Series reactance  "
    )

    b: float = Field(
        title = "b",
        description = "Shunt susceptance "
    )

    tm_ub: float = Field(
        title = "tm_ub",
        description = "Upper bound for off-nominal taps ratio "
    )

    tm_lb: float = Field(
        title = "tm_lb",
        description = "Lower bound for off-nominal taps ratio "
    )

    ta_ub: float = Field(
        title = "ta_ub",
        description = "Upper bound for phase shifting angle "
    )

    ta_lb: float = Field(
        title = "ta_lb",
        description = "Lower bound for phase shifting angle "
    )

    mva_ub_nom: float = Field(
        title = "mva_ub_nom",
        description = "MVA limit, nominal rating "
    )

    mva_ub_sht: Optional[float] = Field(
        title = "mva_ub_sht",
        description = "MVA limit, short term rating "
    )

    mva_ub_em: float = Field(
        title = "mva_ub_em",
        description = "MVA limit, emergency rating "
    )

    # 

    standby_cost: float = Field(
        title = "standby_cost",
        description = "Transformer fixed standby cost "
    )

    connection_cost: float = Field(
        title = "connection_cost",
        description = "Transformer connection cost "
    )

    disconnection_cost: float = Field(
        title = "disconnection_cost",
        description = "Transformer disconnection cost "
    )

    additional_shunt: bool = Field(
        title = "additional_shunt",
        description = "Transformer has additional shunt components "
    )

    # Additional shunt attributes

    g_fr: float = Field(
        title = "g_fr",
        description = "Conductance for shunt component at from bus "
    )

    b_fr: float = Field(
        title = "b_fr",
        description = "Susceptance for shunt component at from bus "
    )

    g_to: float = Field(
        title = "g_to",
        description = "Conductance for shunt component at to bus "
    )

    b_to: float = Field(
        title = "b_to",
        description = "Susceptance for shunt component at to bus "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 

    # 


class DCLine(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "DC line unique identifier "
    )

    fr_bus: str = Field(
        title = "fr_bus",
        description = "Unique identifier for connecting from bus "
    )

    to_bus: str = Field(
        title = "to_bus",
        description = "Unique identifier for connecting to bus "
    )

    pdc_fr_ub: float = Field(
        title = "pdc_fr_ub",
        description = "Maximum active power, from bus "
    )

    pdc_fr_lb: float = Field(
        title = "pdc_fr_lb",
        description = "Minimum active power, from bus "
    )

    qdc_fr_ub: float = Field(
        title = "qdc_fr_ub",
        description = "Maximum reactive power, from bus "
    )

    qdc_fr_lb: float = Field(
        title = "qdc_fr_lb",
        description = "Minimum reactive power, from bus "
    )

    qdc_to_ub: float = Field(
        title = "qdc_to_ub",
        description = "Maximum reactive power, to bus "
    )

    qdc_to_lb: float = Field(
        title = "qdc_to_lb",
        description = "Minimum reactive power, to bus "
    )

    standby_cost: float = Field(
        title = "standby_cost",
        description = "{DC line fixed standby cost "
    )

    connection_cost: float = Field(
        title = "connection_cost",
        description = "{DC line connection cost "
    )

    disconnection_cost: float = Field(
        title = "disconnection_cost",
        description = "{DC line disconnection cost "
    )

    # \end{tabular}

    # \end{center}

    # 


class RegionalReserves(BidDSJsonBaseModel):

    # Active reserve attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REG_UP_vio_cost: float = Field(
        title = "REG_UP_vio_cost",
        description = "Regulation reserve up violation cost "
    )

    REG_DOWN_vio_cost: float = Field(
        title = "REG_DOWN_vio_cost",
        description = "Regulation reserve down violation cost "
    )

    SYN_vio_cost: float = Field(
        title = "SYN_vio_cost",
        description = "Synchronized reserve violation cost "
    )

    NSYN_vio_cost: float = Field(
        title = "NSYN_vio_cost",
        description = "Non-synchronized reserve violation cost "
    )

    # 

    # 

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

    REACT_UP_vio_cost: float = Field(
        title = "REACT_UP_vio_cost",
        description = "Reactive reserve power violation cost "
    )

    REACT_DOWN_vio_cost: float = Field(
        title = "REACT_DOWN_vio_cost",
        description = "Reactive reserve power violation cost "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 


