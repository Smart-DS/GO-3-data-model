import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
from datamodel.input.staticinner import *

class GeneralBase(BidDSJsonBaseModel):

    # Global time attributes

    timestamp_start: Optional[str] = Field(
        title = "timestamp_start",
        description = "Period beginning timestamp for the first interval as string: YYYY-MM-DDThh:mm at UTC "
    )

    timestamp_stop: Optional[str] = Field(
        title = "timestamp_stop",
        description = "Period beginning timestamp for the interval following the last interval as string: YYYY-MM-DDThh:mm at UTC) "
    )

    # Qualitative descriptors

    season: Optional[str] = Field(
        title = "season",
        description = "Season of the year the problem lies within ",
        options = ["Winter", "Spring", "Summer", "Fall"]
    )

    electricity_demand: Optional[str] = Field(
        title = "electricity_demand",
        description = "How demand compares to other times of the year/season ",
        options = ["Peak", "High", "Average", "Low", "Minimum"]
    )

    vre_availability: Optional[str] = Field(
        title = "vre_availability",
        description = "How variable renewable energy availability compares to other times of the year/season ",
        options = ["High", "Average", "Low"]
    )

    solar_availability: Optional[str] = Field(
        title = "solar_availability",
        description = "How solar availability compares to other times of the year/season ",
        options = ["High", "Average", "Low"]
    )

    wind_availability: Optional[str] = Field(
        title = "wind_availability",
        description = "How wind availability compares to other times of the year/season ",
        options = ["High", "Average", "Low"]
    )

    weather_temperature: Optional[str] = Field(
        title = "weather_temperature",
        description = "How outside temperature compares to other times of the year/season ",
        options = ["Hottest", "Warm", "Average", "Cool", "Cold"]
    )

    day_type: Optional[str] = Field(
        title = "day_type",
        description = "What kind of weekday is represented ",
        options = ["Weekday", "Weekend", "Holiday"]
    )

    net_load: Optional[str] = Field(
        title = "net_load",
        description = "How the net-load profile compares to other times of the year/season ",
        options = ["Peak", "High", "Average", "Low", "Minimum", "High-Up-Ramp", "High-Down-Ramp"]
    )

    # Normalization attributes

    base_norm_mva: float = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
    )


class ViolationCostsParametersBase(BidDSJsonBaseModel):

    # Global violation attributes

    p_bus_vio_cost: float = Field(
        title = "p_bus_vio_cost",
        description = "Bus violation costs for active power violation (\$/pu-h) "
    )

    q_bus_vio_cost: float = Field(
        title = "q_bus_vio_cost",
        description = "Bus violation costs for reactive power violation  (\$/pu-h) "
    )

    s_vio_cost: float = Field(
        title = "s_vio_cost",
        description = "Branch violation costs for thermal violation (\$/pu-h) "
    )


class BusBase(BidDSJsonBaseModel):

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
        description = "Bus location - latitude   "
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

    base_nom_volt: float = Field(
        title = "base_nom_volt",
        description = "Bus nominal voltage "
    )

    type: Optional[str] = Field(
        title = "type",
        description = "Bus type ",
        options = ["PQ", "PV", "Slack", "Not_used"]
    )

    initial_status: BusInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )


class ShuntBase(BidDSJsonBaseModel):

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
        description = "Shunt conductance for one step (p.u.) "
    )

    bs: float = Field(
        title = "bs",
        description = "Shunt susceptance for one step (p.u.) "
    )

    step_ub: int = Field(
        title = "step_ub",
        description = "Maximum step number "
    )

    step_lb: int = Field(
        title = "step_lb",
        description = "Minimum step number "
    )

    initial_status: ShuntInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )


class DispatchableDevices_SimpleProducingConsumingDevicesBase(BidDSJsonBaseModel):

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
        options = ["producer", "consumer"]
    )

    description: Optional[str] = Field(
        title = "description",
        description = "Detail description of the device  "
    )

    vm_setpoint: Optional[float] = Field(
        title = "vm_setpoint",
        description = "Voltage magnitude setpoint "
    )

    nameplate_capacity: Optional[float] = Field(
        title = "nameplate_capacity",
        description = "Reference capacity "
    )

    startup_cost: float = Field(
        title = "startup_cost",
        description = "Device start up cost "
    )

    startup_states: List[Tuple[float,float]] = Field(
        title = "startup_states",
        description = "Array of downtime dependent start up states, where each states  is an array with exactly two elements: 1) start up cost adjustments (Float, \$), 2) maximum down time (Float, hr)  "
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

    energy_req_ub: List[Tuple[float,float,float]] = Field(
        title = "energy_req_ub",
        description = "Array of energy upper bound requirement data blocks, where each  data block is an array with exactly three elements:  1) interval starting time (Float, hr), 2) interval ending time (Float, hr), and  3) maximum energy within the interval (Float, p.u.) "
    )

    energy_req_lb: List[Tuple[float,float,float]] = Field(
        title = "energy_req_lb",
        description = "Array of energy lower bound requirement data blocks, where each  data block is an array with exactly three elements:  1) interval starting time (Float, hr), 2) interval ending time (Float, hr), and  3) minimum energy within the interval (Float, p.u.) "
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

    initial_status: DispatchableDevices_SimpleProducingConsumingDevicesInitialStatus = Field(
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

    # Device attributes

    # 

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

    # 


class ACTransmissionLineBase(BidDSJsonBaseModel):

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

    connection_cost: float = Field(
        title = "connection_cost",
        description = "AC Line connection cost "
    )

    disconnection_cost: float = Field(
        title = "disconnection_cost",
        description = "AC line disconnection cost "
    )

    initial_status: ACTransmissionLineInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    additional_shunt: bool = Field(
        title = "additional_shunt",
        description = "Branch has additional shunt components "
    )


class TwoWindingTransformerBase(BidDSJsonBaseModel):

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

    connection_cost: float = Field(
        title = "connection_cost",
        description = "Transformer connection cost "
    )

    disconnection_cost: float = Field(
        title = "disconnection_cost",
        description = "Transformer disconnection cost "
    )

    initial_status: TwoWindingTransformerInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    additional_shunt: bool = Field(
        title = "additional_shunt",
        description = "Transformer has additional shunt components "
    )


class DCLineBase(BidDSJsonBaseModel):

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

    pdc_ub: float = Field(
        title = "pdc_ub",
        description = "Maximum active power "
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

    initial_status: DCLineInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )


class ActiveZonalReserveRequirementsViolationCostsBase(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Zone reserve unique identifier "
    )

    REG_UP: float = Field(
        title = "REG_UP",
        description = "Regulation reserve up requirement fraction "
    )

    REG_DOWN: float = Field(
        title = "REG_DOWN",
        description = "Regulation reserve down requirement faction "
    )

    SYN: float = Field(
        title = "SYN",
        description = "Synchronized reserve requirement fraction "
    )

    NSYN: float = Field(
        title = "NSYN",
        description = "Non-synchronized reserve requirement fraction "
    )

    REG_UP_vio_cost: float = Field(
        title = "REG_UP_vio_cost",
        description = "Regulation reserve up violation cost (\$/pu-hr) "
    )

    REG_DOWN_vio_cost: float = Field(
        title = "REG_DOWN_vio_cost",
        description = "Regulation reserve down violation cost (\$/pu-hr) "
    )

    SYN_vio_cost: float = Field(
        title = "SYN_vio_cost",
        description = "Synchronized reserve violation cost (\$/pu-hr) "
    )

    NSYN_vio_cost: float = Field(
        title = "NSYN_vio_cost",
        description = "Non-synchronized reserve violation cost (\$/pu-hr) "
    )

    RAMPING_RESERVE_UP_vio_cost: float = Field(
        title = "RAMPING_RESERVE_UP_vio_cost",
        description = "Flexible-ramp up violation cost (\$/pu-hr) "
    )

    RAMPING_RESERVE_DOWN_vio_cost: float = Field(
        title = "RAMPING_RESERVE_DOWN_vio_cost",
        description = "Flexible-ramp down violation cost (\$/pu-hr) "
    )


class ReactiveZonalReserveRequirementsViolationCostsBase(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REACT_UP_vio_cost: float = Field(
        title = "REACT_UP_vio_cost",
        description = "Reactive reserve power violation cost (\$/pu-hr) "
    )

    REACT_DOWN_vio_cost: float = Field(
        title = "REACT_DOWN_vio_cost",
        description = "Reactive reserve power violation cost (\$/pu-hr) "
    )


