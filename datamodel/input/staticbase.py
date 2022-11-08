import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel
from datamodel.input.staticinner import *

class GeneralBase(BidDSJsonBaseModel):

    # Global time attributes

    timestamp_start: Optional[str] = Field(
        title = "timestamp_start",
        description = "Period beginning timestamp for the first interval as string: YYYY-MM-DDThh:mm:ss at UTC "
    )

    timestamp_stop: Optional[str] = Field(
        title = "timestamp_stop",
        description = "Period beginning timestamp for the interval following the last interval as string: YYYY-MM-DDThh:mm:ss at UTC "
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

    base_norm_mva: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
    )


class ViolationCostsParametersBase(BidDSJsonBaseModel):

    # Global violation attributes

    p_bus_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_bus_vio_cost",
        description = "Bus violation costs for active power violation in \$/pu-h "
    )

    q_bus_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "q_bus_vio_cost",
        description = "Bus violation costs for reactive power violation in \$/pu-h "
    )

    s_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "s_vio_cost",
        description = "Branch violation costs for thermal violation in \$/pu-h "
    )

    e_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "e_vio_cost",
        description = "Energy violation costs for energy constraint violation in \$/pu-h "
    )


class BusBase(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Bus unique identifier "
    )

    vm_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "vm_ub",
        description = "Voltage magnitude upper bound in p.u. "
    )

    vm_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "vm_lb",
        description = "Voltage magnitude lower bound in p.u. "
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

    longitude: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "longitude",
        description = "Bus location - longitude in decimal degree "
    )

    latitude: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "latitude",
        description = "Bus location - latitude in decimal degree "
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

    con_loss_factor: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "con_loss_factor",
        description = "Contingency participation loss factor "
    )

    base_nom_volt: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
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

    gs: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "gs",
        description = "Shunt conductance for one step in p.u. "
    )

    bs: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "bs",
        description = "Shunt susceptance for one step in p.u. "
    )

    step_ub: StrictInt = Field(
        title = "step_ub",
        description = "Maximum step number "
    )

    step_lb: StrictInt = Field(
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

    vm_setpoint: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "vm_setpoint",
        description = "Voltage magnitude setpoint in p.u. "
    )

    nameplate_capacity: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "nameplate_capacity",
        description = "Reference capacity in p.u. "
    )

    startup_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "startup_cost",
        description = "Device start up cost in \$ "
    )

    startup_states: List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]] = Field(
        title = "startup_states",
        description = "Array of downtime dependent start up states, where each states  is an array with exactly two elements: 1) start up cost adjustments in \$ (Float), 2) maximum down time in hr (Float)  "
    )

    shutdown_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "shutdown_cost",
        description = "Device shut down cost in \$ "
    )

    startups_ub: List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False), StrictInt]] = Field(
        title = "startups_ub",
        description = "Array of time interval startup data blocks, where each  data block is an array with exactly three elements:  1) interval starting time in hr (Float), 2) interval ending time in hr (Float), and  3) maximum startups within the interval (Int) "
    )

    # 

    energy_req_ub: List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]] = Field(
        title = "energy_req_ub",
        description = "Array of energy upper bound requirement data blocks, where each  data block is an array with exactly three elements:  1) interval starting time in hr (Float), 2) interval ending time in hr (Float), and  3) maximum energy within the interval in p.u. (Float) "
    )

    energy_req_lb: List[Tuple[confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False), confloat(gt=-float('inf'), lt=float('inf'), strict=False)]] = Field(
        title = "energy_req_lb",
        description = "Array of energy lower bound requirement data blocks, where each  data block is an array with exactly three elements:  1) interval starting time in hr (Float), 2) interval ending time in hr (Float), and  3) minimum energy within the interval in p.u. (Float) "
    )

    on_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "on_cost",
        description = "Device fixed operating cost in \$ "
    )

    in_service_time_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "in_service_time_lb",
        description = "Minimum uptime in service in hr "
    )

    down_time_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "down_time_lb",
        description = "Minimum downtime in hr "
    )

    p_ramp_up_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_ramp_up_ub",
        description = "{(Case: producer) Max production ramp up when operating in p.u./hr (Float)}  {(Case: consumer) Max consumption ramp up when operating in p.u./hr "
    )

    p_ramp_down_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_ramp_down_ub",
        description = "{(Case: producer) Max production ramp down when operating in p.u./hr (Float)}  {(Case: consumer) Max consumption ramp down when operating in p.u./hr "
    )

    p_startup_ramp_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_startup_ramp_ub",
        description = "{(Case: producer) Max production ramp up when start up in p.u./hr (Float)}  {(Case: consumer) Max consumption ramp up when start up in p.u./hr "
    )

    p_shutdown_ramp_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_shutdown_ramp_ub",
        description = "{(Case: producer) Max production ramp down when shut down in p.u./hr (Float)}  {(Case: consumer) Max consumption ramp down when shut down in p.u./hr "
    )

    initial_status: DispatchableDevices_SimpleProducingConsumingDevicesInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data for initial time step "
    )

    # Flags for extra parameters

    q_linear_cap: conint(ge=0, le=1, strict=True) = Field(
        title = "q_linear_cap",
        description = "Device has additional reactive constraint "
    )

    q_bound_cap: conint(ge=0, le=1, strict=True) = Field(
        title = "q_bound_cap",
        description = "Device has additional reactive bounds "
    )

    # Device attributes

    # Reserve attributes

    p_reg_res_up_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_reg_res_up_ub",
        description = "Maximum regulation reserve up in p.u. "
    )

    p_reg_res_down_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_reg_res_down_ub",
        description = "Maximum regulation reserve down in p.u. "
    )

    p_syn_res_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_syn_res_ub",
        description = "Maximum synchronized reserve in p.u. "
    )

    p_nsyn_res_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_nsyn_res_ub",
        description = "Maximum non-synchronized reserve in p.u. "
    )

    p_ramp_res_up_online_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_ramp_res_up_online_ub",
        description = "Maximum ramp up reserve when online in p.u. "
    )

    p_ramp_res_down_online_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_ramp_res_down_online_ub",
        description = "Maximum ramp down reserve when online in p.u. "
    )

    p_ramp_res_up_offline_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_ramp_res_up_offline_ub",
        description = "Maximum ramp up reserve when offline in p.u. "
    )

    p_ramp_res_down_offline_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "p_ramp_res_down_offline_ub",
        description = "Maximum ramp down reserve when offline in p.u. "
    )

    # Time varying reserve attributes

    # 

    q_0: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_0",
        description = "{ (Case: producer) Reactive production at zero active production in p.u. (Float) } { (Case: consumer) Reactive consumption at zero active consumption in p.u. "
    )

    beta: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "beta",
        description = "Slope of active-reactive capability curve "
    )

    q_0_ub: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_0_ub",
        description = "{ (Case: producer) Max reactive production at zero active production in p.u. (Float)}  { (Case: consumer) Max reactive consumption at zero active consumption in p.u. "
    )

    q_0_lb: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "q_0_lb",
        description = "{ (Case: producer) Min reactive production at zero active production in p.u. (Float)}  { (Case: consumer) Min reactive consumption at zero active consumption in p.u. "
    )

    beta_ub: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "beta_ub",
        description = "Upper bound for slope of active-reactive capability curve "
    )

    beta_lb: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "beta_lb",
        description = "Lower bound for slope of active-reactive capability curve "
    )

    @root_validator(pre=False)
    def check_conditional_q_0(cls, values):
        if values.get("q_linear_cap") is not None and values.get("q_linear_cap") == 1 and values.get("q_0") is None:
             raise ValueError("Conditional element q_0 is missing when q_linear_cap is 1")
        if values.get("q_linear_cap") is not None and values.get("q_linear_cap") != 1 and values.get("q_0") is not None:
             raise ValueError("Conditional element q_0 is present when q_linear_cap is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_beta(cls, values):
        if values.get("q_linear_cap") is not None and values.get("q_linear_cap") == 1 and values.get("beta") is None:
             raise ValueError("Conditional element beta is missing when q_linear_cap is 1")
        if values.get("q_linear_cap") is not None and values.get("q_linear_cap") != 1 and values.get("beta") is not None:
             raise ValueError("Conditional element beta is present when q_linear_cap is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_q_0_ub(cls, values):
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") == 1 and values.get("q_0_ub") is None:
             raise ValueError("Conditional element q_0_ub is missing when q_bound_cap is 1")
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") != 1 and values.get("q_0_ub") is not None:
             raise ValueError("Conditional element q_0_ub is present when q_bound_cap is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_q_0_lb(cls, values):
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") == 1 and values.get("q_0_lb") is None:
             raise ValueError("Conditional element q_0_lb is missing when q_bound_cap is 1")
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") != 1 and values.get("q_0_lb") is not None:
             raise ValueError("Conditional element q_0_lb is present when q_bound_cap is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_beta_ub(cls, values):
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") == 1 and values.get("beta_ub") is None:
             raise ValueError("Conditional element beta_ub is missing when q_bound_cap is 1")
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") != 1 and values.get("beta_ub") is not None:
             raise ValueError("Conditional element beta_ub is present when q_bound_cap is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_beta_lb(cls, values):
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") == 1 and values.get("beta_lb") is None:
             raise ValueError("Conditional element beta_lb is missing when q_bound_cap is 1")
        if values.get("q_bound_cap") is not None and values.get("q_bound_cap") != 1 and values.get("beta_lb") is not None:
             raise ValueError("Conditional element beta_lb is present when q_bound_cap is not 1")
        return values

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

    r: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "r",
        description = "Series resistance in p.u. "
    )

    x: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "x",
        description = "Series reactance  in p.u. "
    )

    b: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "b",
        description = "Shunt susceptance in p.u. "
    )

    mva_ub_nom: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "mva_ub_nom",
        description = "MVA limit, nominal rating in p.u. "
    )

    mva_ub_sht: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "mva_ub_sht",
        description = "MVA limit, short term rating in p.u. "
    )

    mva_ub_em: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "mva_ub_em",
        description = "MVA limit, emergency rating in p.u. "
    )

    connection_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "connection_cost",
        description = "AC Line connection cost in \$ "
    )

    disconnection_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "disconnection_cost",
        description = "AC line disconnection cost in \$ "
    )

    initial_status: ACTransmissionLineInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    additional_shunt: conint(ge=0, le=1, strict=True) = Field(
        title = "additional_shunt",
        description = "Branch has additional shunt components "
    )

    g_fr: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "g_fr",
        description = "Conductance for shunt component at from bus in p.u. "
    )

    b_fr: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "b_fr",
        description = "Susceptance for shunt component at from bus in p.u. "
    )

    g_to: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "g_to",
        description = "Conductance for shunt component at to bus in p.u. "
    )

    b_to: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "b_to",
        description = "Susceptance for shunt component at to bus in p.u. "
    )

    @root_validator(pre=False)
    def check_conditional_g_fr(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("g_fr") is None:
             raise ValueError("Conditional element g_fr is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("g_fr") is not None:
             raise ValueError("Conditional element g_fr is present when additional_shunt is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_b_fr(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("b_fr") is None:
             raise ValueError("Conditional element b_fr is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("b_fr") is not None:
             raise ValueError("Conditional element b_fr is present when additional_shunt is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_g_to(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("g_to") is None:
             raise ValueError("Conditional element g_to is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("g_to") is not None:
             raise ValueError("Conditional element g_to is present when additional_shunt is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_b_to(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("b_to") is None:
             raise ValueError("Conditional element b_to is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("b_to") is not None:
             raise ValueError("Conditional element b_to is present when additional_shunt is not 1")
        return values

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

    r: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "r",
        description = "Series resistance in p.u. "
    )

    x: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "x",
        description = "Series reactance  in p.u. "
    )

    b: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "b",
        description = "Shunt susceptance in p.u. "
    )

    tm_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "tm_ub",
        description = "Upper bound for off-nominal tap ratio in p.u. "
    )

    tm_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "tm_lb",
        description = "Lower bound for off-nominal tap ratio in p.u. "
    )

    ta_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "ta_ub",
        description = "Upper bound for phase shifting angle in radian "
    )

    ta_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "ta_lb",
        description = "Lower bound for phase shifting angle in radian "
    )

    mva_ub_nom: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "mva_ub_nom",
        description = "MVA limit, nominal rating in p.u. "
    )

    mva_ub_sht: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "mva_ub_sht",
        description = "MVA limit, short term rating in p.u. "
    )

    mva_ub_em: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "mva_ub_em",
        description = "MVA limit, emergency rating in p.u. "
    )

    connection_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "connection_cost",
        description = "Transformer connection cost in \$ "
    )

    disconnection_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "disconnection_cost",
        description = "Transformer disconnection cost in \$ "
    )

    initial_status: TwoWindingTransformerInitialStatus = Field(
        title = "initial_status",
        description = "A JSON inner object storing data   for initial time step "
    )

    additional_shunt: conint(ge=0, le=1, strict=True) = Field(
        title = "additional_shunt",
        description = "Transformer has additional shunt components "
    )

    g_fr: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "g_fr",
        description = "Conductance for shunt component at from bus in p.u. "
    )

    b_fr: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "b_fr",
        description = "Susceptance for shunt component at from bus in p.u. "
    )

    g_to: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "g_to",
        description = "Conductance for shunt component at to bus in p.u. "
    )

    b_to: Optional[confloat(gt=-float('inf'), lt=float('inf'), strict=False)] = Field(
        title = "b_to",
        description = "Susceptance for shunt component at to bus in p.u. "
    )

    @root_validator(pre=False)
    def check_conditional_g_fr(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("g_fr") is None:
             raise ValueError("Conditional element g_fr is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("g_fr") is not None:
             raise ValueError("Conditional element g_fr is present when additional_shunt is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_b_fr(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("b_fr") is None:
             raise ValueError("Conditional element b_fr is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("b_fr") is not None:
             raise ValueError("Conditional element b_fr is present when additional_shunt is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_g_to(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("g_to") is None:
             raise ValueError("Conditional element g_to is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("g_to") is not None:
             raise ValueError("Conditional element g_to is present when additional_shunt is not 1")
        return values
    @root_validator(pre=False)
    def check_conditional_b_to(cls, values):
        if values.get("additional_shunt") is not None and values.get("additional_shunt") == 1 and values.get("b_to") is None:
             raise ValueError("Conditional element b_to is missing when additional_shunt is 1")
        if values.get("additional_shunt") is not None and values.get("additional_shunt") != 1 and values.get("b_to") is not None:
             raise ValueError("Conditional element b_to is present when additional_shunt is not 1")
        return values

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

    pdc_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "pdc_ub",
        description = "Maximum active power in p.u. "
    )

    qdc_fr_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "qdc_fr_ub",
        description = "Maximum reactive power, from bus in p.u. "
    )

    qdc_fr_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "qdc_fr_lb",
        description = "Minimum reactive power, from bus in p.u. "
    )

    qdc_to_ub: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "qdc_to_ub",
        description = "Maximum reactive power, to bus in p.u. "
    )

    qdc_to_lb: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "qdc_to_lb",
        description = "Minimum reactive power, to bus in p.u. "
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

    REG_UP: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "REG_UP",
        description = "Regulation reserve up requirement fraction "
    )

    REG_DOWN: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "REG_DOWN",
        description = "Regulation reserve down requirement faction "
    )

    SYN: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "SYN",
        description = "Synchronized reserve requirement fraction "
    )

    NSYN: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "NSYN",
        description = "Non-synchronized reserve requirement fraction "
    )

    REG_UP_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "REG_UP_vio_cost",
        description = "Regulation reserve up violation cost in \$/pu-hr "
    )

    REG_DOWN_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "REG_DOWN_vio_cost",
        description = "Regulation reserve down violation cost in \$/pu-hr "
    )

    SYN_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "SYN_vio_cost",
        description = "Synchronized reserve violation cost in \$/pu-hr "
    )

    NSYN_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "NSYN_vio_cost",
        description = "Non-synchronized reserve violation cost in \$/pu-hr "
    )

    RAMPING_RESERVE_UP_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "RAMPING_RESERVE_UP_vio_cost",
        description = "Flexible-ramp up violation cost in \$/pu-hr "
    )

    RAMPING_RESERVE_DOWN_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "RAMPING_RESERVE_DOWN_vio_cost",
        description = "Flexible-ramp down violation cost in \$/pu-hr "
    )


class ReactiveZonalReserveRequirementsViolationCostsBase(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    REACT_UP_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "REACT_UP_vio_cost",
        description = "Reactive reserve power violation cost in \$/pu-hr "
    )

    REACT_DOWN_vio_cost: confloat(gt=-float('inf'), lt=float('inf'), strict=False) = Field(
        title = "REACT_DOWN_vio_cost",
        description = "Reactive reserve power violation cost in \$/pu-hr "
    )


