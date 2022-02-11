import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import String, Dict, List, Optional, Union

from datamodel.base import BidDSJsonBaseModel

class General(BidDSJsonBaseModel):

    # Global time attributes

    # Normalization attributes

    base_norm_mva: Optional[float] = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
    )


class ViolationCostsParameters(BidDSJsonBaseModel):

    # Global violation attributes

    p_bus_vio_cost: float = Field(
        title = "p_bus_vio_cost",
        description = "Bus marginal costs for active power violation "
    )

    q_bus_vio_cost: float = Field(
        title = "q_bus_vio_cost",
        description = "Bus marginal costs for reactive power violation  "
    )

    v_bus_vio_cost: float = Field(
        title = "v_bus_vio_cost",
        description = "Bus marginal costs for voltage violation "
    )

    mva_branch_vio_cost: float = Field(
        title = "mva_branch_vio_cost",
        description = "Branch marginal costs for thermal violation "
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

    type: Optional[String] = Field(
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


class ProducingDevices_SingleModeGeneratingUnits(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    bus: str = Field(
        title = "bus",
        description = "Unique identifier for connecting bus "
    )

    vm_setpoint: Optional[float] = Field(
        title = "vm_setpoint",
        description = "Voltage magnitude setpoint "
    )

    startup_cost: float = Field(
        title = "startup_cost",
        description = "Producing device startup cost "
    )

    shutdown_cost: float = Field(
        title = "shutdown_cost",
        description = "Producing device shutdown cost "
    )

    startup_num_ub: int = Field(
        title = "startup_num_ub",
        description = "Maximum startups "
    )

    # 

    # 

    # 

    on_cost: float = Field(
        title = "on_cost",
        description = "Producing device fixed operating cost "
    )

    in_service_time_lb: float = Field(
        title = "in_service_time_lb",
        description = "Minimum uptime (hr) to operate/in service "
    )

    down_time_lb: float = Field(
        title = "down_time_lb",
        description = "Minimum (hr) downtime "
    )

    pg_ramp_ub: float = Field(
        title = "pg_ramp_ub",
        description = "Maximum ramp up on operating cond."
    )

    pg_ramp_lb: float = Field(
        title = "pg_ramp_lb",
        description = "Maximum ramp down on operating cond."
    )

    pg_startup_ramp_ub: float = Field(
        title = "pg_startup_ramp_ub",
        description = "Maximum ramp up on startup "
    )

    pg_shutdown_ramp_lb: float = Field(
        title = "pg_shutdown_ramp_lb",
        description = "Maximum ramp down on shutdown "
    )

    pg_regulation_up_ub: float = Field(
        title = "pg_regulation_up_ub",
        description = "Maximum regulation up reserve "
    )

    pg_regulation_down_ub: float = Field(
        title = "pg_regulation_down_ub",
        description = "Maximum regulation down reserve "
    )

    pg_spin_ub: float = Field(
        title = "pg_spin_ub",
        description = "Maximum spinning reserve "
    )

    pg_nonspin_ub: float = Field(
        title = "pg_nonspin_ub",
        description = "Maximum non-spinning reserve "
    )

    pg_flexi_up_online_ub: float = Field(
        title = "pg_flexi_up_online_ub",
        description = "Maximum flexible ramp up reserve when online "
    )

    pg_flexi_down_online_ub: float = Field(
        title = "pg_flexi_down_online_ub",
        description = "Maximum flexible ramp down reserve when online "
    )

    pg_flexi_up_offline_ub: float = Field(
        title = "pg_flexi_up_offline_ub",
        description = "Maximum flexible ramp up reserve when offline "
    )

    pg_flexi_down_offline_ub: float = Field(
        title = "pg_flexi_down_offline_ub",
        description = "Maximum flexible ramp down reserve when offline "
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


class ProducingDevices_MultipleModeGeneratingUnits(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Producing device unique identifier "
    )

    bus: str = Field(
        title = "bus",
        description = "Unique identifier for connecting bus "
    )

    vm_setpoint: Optional[float] = Field(
        title = "vm_setpoint",
        description = "Voltage magnitude setpoint "
    )

    startup_cost: float = Field(
        title = "startup_cost",
        description = "Producing device startup cost "
    )

    shutdown_cost: float = Field(
        title = "shutdown_cost",
        description = "Producing device shutdown cost "
    )

    startup_num_ub: int = Field(
        title = "startup_num_ub",
        description = "Maximum startups "
    )

    in_service_time_lb: float = Field(
        title = "in_service_time_lb",
        description = "Minimum uptime (hr) to operate/in service "
    )

    down_time_lb: float = Field(
        title = "down_time_lb",
        description = "Minimum (hr) downtime "
    )

    pg_startup_ramp_ub: float = Field(
        title = "pg_startup_ramp_ub",
        description = "Maximum ramp up on startup "
    )

    pg_shutdown_ramp_lb: float = Field(
        title = "pg_shutdown_ramp_lb",
        description = "Maximum ramp down on shutdown "
    )

    pg_regulation_up_ub: float = Field(
        title = "pg_regulation_up_ub",
        description = "Maximum regulation up reserve "
    )

    pg_regulation_down_ub: float = Field(
        title = "pg_regulation_down_ub",
        description = "Maximum regulation down reserve "
    )

    pg_spin_ub: float = Field(
        title = "pg_spin_ub",
        description = "Maximum spinning reserve "
    )

    pg_nonspin_ub: float = Field(
        title = "pg_nonspin_ub",
        description = "Maximum non-spinning reserve "
    )

    pg_flexi_up_online_ub: float = Field(
        title = "pg_flexi_up_online_ub",
        description = "Maximum flexible ramp up reserve when online "
    )

    pg_flexi_down_online_ub: float = Field(
        title = "pg_flexi_down_online_ub",
        description = "Maximum flexible ramp down reserve when online "
    )

    pg_flexi_up_offline_ub: float = Field(
        title = "pg_flexi_up_offline_ub",
        description = "Maximum flexible ramp up reserve when offline "
    )

    pg_flexi_down_offline_ub: float = Field(
        title = "pg_flexi_down_offline_ub",
        description = "Maximum flexible ramp down reserve when offline "
    )

    # \hline \hline

    # Initial status attributes within:

    on_status: int = Field(
        title = "on_status",
        description = "On status indicator for initial time step ",
        options = [0, 1]
    )

    select_mode: str = Field(
        title = "select_mode",
        description = "Active mode uid for initial time step "
    )

    pg: float = Field(
        title = "pg",
        description = "Active dispatch for initial time step "
    )

    qg: float = Field(
        title = "qg",
        description = "Reactive dispatch for initial time step "
    )

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

    # \hline \hline

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

    # \hline \hline

    # \end{tabular}

    # \end{center}

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Mode attributes

    mode_num: int = Field(
        title = "mode_num",
        description = "Number of operating modes "
    )

    # Inner mode attributes ---

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

    on_cost: float = Field(
        title = "on_cost",
        description = "Mode fixed operating cost "
    )

    # 

    pg_ramp_ub: float = Field(
        title = "pg_ramp_ub",
        description = "Maximum ramp up on operating cond."
    )

    pg_ramp_lb: float = Field(
        title = "pg_ramp_lb",
        description = "Maximum ramp down on operating cond."
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

    b_ch: float = Field(
        title = "b_ch",
        description = "AC line charging susceptance "
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

    b_lk: float = Field(
        title = "b_lk",
        description = "Susceptance for transformer leakage "
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

    SPIN: float = Field(
        title = "SPIN",
        description = "Spinning reserve requirement "
    )

    NON_SPIN: float = Field(
        title = "NON_SPIN",
        description = "Non-spinning reserve requirement "
    )

    FLEXI_RAMP_UP: float = Field(
        title = "FLEXI_RAMP_UP",
        description = "Flexible-ramp up requirement "
    )

    FLEXI_RAMP_DOWN: float = Field(
        title = "FLEXI_RAMP_DOWN",
        description = "Flexible-ramp down requirement "
    )

    REG_UP_cost: float = Field(
        title = "REG_UP_cost",
        description = "Regulation reserve up marginal cost "
    )

    REG_DOWN_cost: float = Field(
        title = "REG_DOWN_cost",
        description = "Regulation reserve down marginal cost "
    )

    SPIN_cost: float = Field(
        title = "SPIN_cost",
        description = "Spinning reserve marginal cost "
    )

    NON_SPIN_cost: float = Field(
        title = "NON_SPIN_cost",
        description = "Non-spinning reserve marginal cost "
    )

    # 

    # 

    # 

    # 


