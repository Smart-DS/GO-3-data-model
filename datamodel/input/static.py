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

    timestamp_start: Optional[str] = Field(
        title = "timestamp_start",
        description = "Period beginning timestamp for the first interval "
    )

    timestamp_stop: Optional[str] = Field(
        title = "timestamp_stop",
        description = "Period beginning timestamp for the interval following the last interval "
    )

    # Qualitative descriptors

    season: Optional[str] = Field(
        title = "season",
        description = "Season of the year the problem lies within ",
        options = ["Winter"]
    )

    electricity_demand: Optional[str] = Field(
        title = "electricity_demand",
        description = "How demand compares to other times of the year/season ",
        options = ["Peak"]
    )

    vre_availability: Optional[str] = Field(
        title = "vre_availability",
        description = "How variable renewable energy availability compares to other times of the year/season ",
        options = ["High"]
    )

    solar_availability: Optional[str] = Field(
        title = "solar_availability",
        description = "How solar availablity compares to other times of the year/season ",
        options = ["High"]
    )

    wind_availability: Optional[str] = Field(
        title = "wind_availability",
        description = "How solar availablity compares to other times of the year/season ",
        options = ["High"]
    )

    weather_temperature: Optional[str] = Field(
        title = "weather_temperature",
        description = "How outside temperature compares to other times of the year/season ",
        options = ["Hottest"]
    )

    day_type: Optional[str] = Field(
        title = "day_type",
        description = "What kind of weekday is represented ",
        options = ["Weekday"]
    )

    net_load: Optional[str] = Field(
        title = "net_load",
        description = "How the net-load profile compares to other times of the year/season ",
        options = ["Peak"]
    )

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


class Bus_initial_status(BidDSJsonBaseModel):

    vm: float = Field(
        title = "vm",
        description = "Bus voltage magnitude "
    )

    va: float = Field(
        title = "va",
        description = "Bus voltage angle     "
    )
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

    active_reserve_uids: List[str] = Field(
        title = "active_reserve_uids",
        description = "List of active reserve zones (uids) that the bus participating   "
    )

    reactive_reserve_uids: List[str] = Field(
        title = "reactive_reserve_uids",
        description = "List of reactive reserve zones (uids) that the bus participating   "
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

    # Operations information

    con_loss_factor: Optional[float] = Field(
        title = "con_loss_factor",
        description = "Contingency participation loss factor "
    )

    base_nom_volt: Optional[float] = Field(
        title = "base_nom_volt",
        description = "Bus nominal voltage "
    )

    type: Optional[str] = Field(
        title = "type",
        description = "Bus type ",
        options = ["PQ"]
    )

    initial_status: Bus_initial_status = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    # Initial condition attributes

    vm: float = Field(
        title = "vm",
        description = "Bus voltage magnitude "
    )

    va: float = Field(
        title = "va",
        description = "Bus voltage angle     "
    )

    # \end{tabular}

    # \end{center}


class Shunt_initial_status(BidDSJsonBaseModel):

    on_status: int = Field(
        title = "on_status",
        description = "On-off status ",
        options = [0, 1]
    )

    step: int = Field(
        title = "step",
        description = "Number of step "
    )
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

    step_ub: int = Field(
        title = "step_ub",
        description = "Maximum step number "
    )

    step_lb: int = Field(
        title = "step_lb",
        description = "Minimum step number "
    )

    initial_status: Shunt_initial_status = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    # Initial condition attributes

    on_status: int = Field(
        title = "on_status",
        description = "On-off status ",
        options = [0, 1]
    )

    step: int = Field(
        title = "step",
        description = "Number of step "
    )

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

    bus: str = Field(
        title = "bus",
        description = "Unique identifier for connecting bus "
    )

    device_type: str = Field(
        title = "device_type",
        description = "Type of device ",
        options = ["producer / consumer"]
    )

    description: Optional[str] = Field(
        title = "description",
        description = "Detail description of the device  "
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

    startups_ub: List[Tuple[float,float,int]] = Field(
        title = "startups_ub",
        description = "Array of time interval startup data blocks, where each  data block is an array with exactly three elements:  1) interval starting time (Float, hr), 2) interval ending time (Float, hr), and  3) maximum startups within the interval (Int) "
    )

    # 

    energy_req_ub: float = Field(
        title = "energy_req_ub",
        description = "Array of energy upper bound requirement data blocks, where each  data block is an array with exactly three elements:  1) interval starting time (Float, hr), 2) interval ending time (Float, hr), and  3) maximum energy within the interval "
    )

    energy_req_lb: float = Field(
        title = "energy_req_lb",
        description = "Array of energy lower bound requirement data blocks, where each  data block is an array with exactly three elements:  1) interval starting time (Float, hr), 2) interval ending time (Float, hr), and  3) minimum energy within the interval "
    )

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
        description = "{(Case: producer) Max production ramp up when operating (Float, p.u./hr)}  {(Case: consumer) Max consumption ramp up when operating "
    )

    p_ramp_down_ub: float = Field(
        title = "p_ramp_down_ub",
        description = "{(Case: producer) Max production ramp down when operating (Float, pu/hr)}  {(Case: consumer) Max consumption ramp down when operating "
    )

    p_startup_ramp_ub: float = Field(
        title = "p_startup_ramp_ub",
        description = "{(Case: producer) Max production ramp up when start up (Float, p.u./hr)}  {(Case: consumer) Max consumption ramp up when start up "
    )

    p_shutdown_ramp_ub: float = Field(
        title = "p_shutdown_ramp_ub",
        description = "{(Case: producer) Max production ramp down when shut down (Float, pu/hr)}  {(Case: consumer) Max consumption ramp down when shut down "
    )

    # 

    initial_status: DispatchableDevices_SimpleProducingConsumingDevices_initial_status = Field(
        title = "initial_status",
        description = "A JSON inner object storing data for initial time step "
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

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Device attributes

    # 

    # \end{tabular}

    # \end{center}

    # 

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

    # Time varying reserve attributes

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

    # Reactive cap. attributes

    q_0: float = Field(
        title = "q_0",
        description = "{ (Case: producer) Reactive production at zero active production (Float, p.u.) } { (Case: consumer) Reactive consumption at zero active consumption "
    )

    beta: float = Field(
        title = "beta",
        description = "Slope of active-reactive capability curve "
    )

    # Reactive cap. attributes

    q_0_ub: float = Field(
        title = "q_0_ub",
        description = "{ (Case: producer) Max reactive production at zero active production (Float, p.u.)}  { (Case: consumer) Max reactive consumption at zero active consumption "
    )

    q_0_lb: float = Field(
        title = "q_0_lb",
        description = "{ (Case: producer) Min reactive production at zero active production (Float, p.u.)}  { (Case: consumer) Min reactive consumption at zero active consumption "
    )

    # 

    beta_ub: float = Field(
        title = "beta_ub",
        description = "Upper bound for slope of active-reactive capability curve "
    )

    beta_lb: float = Field(
        title = "beta_lb",
        description = "Lower bound for slope of active-reactive capability curve "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 


class ACTransmissionLine_initial_status(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
        description = "Connection status "
    )
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

    initial_status: ACTransmissionLine_initial_status = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    additional_shunt: int = Field(
        title = "additional_shunt",
        description = "Branch has additional shunt components ",
        options = [0, 1]
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

    # Initial condition attributes

    on_status: bool = Field(
        title = "on_status",
        description = "Connection status "
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 


class TwoWindingTransformer_initial_status(BidDSJsonBaseModel):

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
        description = "Upper bound for off-nominal tap ratio "
    )

    tm_lb: float = Field(
        title = "tm_lb",
        description = "Lower bound for off-nominal tap ratio "
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

    initial_status: TwoWindingTransformer_initial_status = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    additional_shunt: int = Field(
        title = "additional_shunt",
        description = "Transformer has additional shunt components ",
        options = [0, 1]
    )

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

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

    # Initial condition attributes

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

    # \end{tabular}

    # \end{center}

    # 

    # 

    # 

    # 


class DCLine_initial_status(BidDSJsonBaseModel):

    on_status: bool = Field(
        title = "on_status",
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

    initial_status: DCLine_initial_status = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    # Initial condition attributes

    on_status: bool = Field(
        title = "on_status",
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


class ZonalReserveRequirementsViolationCosts(BidDSJsonBaseModel):

    # Active zonal reserve attributes

    uid: str = Field(
        title = "uid",
        description = "Zone reserve unique identifier "
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

    RAMPING_RESERVE_UP_vio_cost: float = Field(
        title = "RAMPING_RESERVE_UP_vio_cost",
        description = "Flexible-ramp up violation cost "
    )

    RAMPING_RESERVE_DOWN_vio_cost: float = Field(
        title = "RAMPING_RESERVE_DOWN_vio_cost",
        description = "Flexible-ramp down violation cost "
    )

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Reactive zonal reserve attributes

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

    # 


