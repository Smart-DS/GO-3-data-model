# Input Objects ----------------------------------------------------------------

# ------ Static ----------------------------------------------------------------

class General(BidDSJsonBaseModel):

    # Global time attributes

    # Global violation attributes

    p_vio_cost: float = Field(
        title = "p_vio_cost",
        description = "System violation costs for active power violation "
    )

    q_vio_cost: float = Field(
        title = "q_vio_cost",
        description = "System violation costs for reactive power violation "
    )

    p_bus_vio_cost: float = Field(
        title = "p_bus_vio_cost",
        description = "Bus violation costs for active power violation "
    )

    q_bus_vio_cost: float = Field(
        title = "q_bus_vio_cost",
        description = "Bus violation costs for reactive power violation  "
    )

    v_bus_vio_cost: Optional[float] = Field(
        title = "v_bus_vio_cost",
        description = "Bus violation costs for voltage violation "
    )

    mva_branch_vio_cost: float = Field(
        title = "mva_branch_vio_cost",
        description = "Branch violation costs for thermal violation "
    )

    # Optional attributes

    base_norm_mva: Optional[float] = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
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

    # {\color{red} {\tt con\_loss\_factor}}

    area: str = Field(
        title = "area",
        description = "Bus control area "
    )

    zone: str = Field(
        title = "zone",
        description = "Bus control zone "
    )

    # 

    # Location/Operation information

    base_nom_volt: Optional[float] = Field(
        title = "base_nom_volt",
        description = "Bus nominal voltage "
    )

    type: Optional[String] = Field(
        title = "type",
        description = "Bus type ",
        options = ["PQ", "PV", "Slack", "Not_used"]
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

    state: Optional[str] = Field(
        title = "state",
        description = "Bus state location "
    )

    country: Optional[str] = Field(
        title = "country",
        description = "Bus country location "
    )

    # 


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
        description = "Shunt conductance "
    )

    bs: float = Field(
        title = "bs",
        description = "Shunt susceptance "
    )

    steps_ub: int = Field(
        title = "steps_ub",
        description = "Maximum number of steps "
    )

    steps_lb: int = Field(
        title = "steps_lb",
        description = "Minimum number of steps "
    )


class DispatchableDevices:GeneratingUnits,LoadDemands,andStorageDevices(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Dispatchable device unique identifier "
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
        description = "Dispatchable device startup cost "
    )

    shutdown_cost: float = Field(
        title = "shutdown_cost",
        description = "Dispatchable device shutdown cost "
    )

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

    config_num: int = Field(
        title = "config_num",
        description = "Number of operating modes/configurations "
    )

    # \hline \hline

    # Initial status attributes within:

    on_status_ub: int = Field(
        title = "on_status_ub",
        description = "On status indicator upper bound for initial time step ",
        options = [0, 1]
    )

    on_status_lb: int = Field(
        title = "on_status_lb",
        description = "On status indicator lower bound for initial time step ",
        options = [0, 1]
    )

    select_config: str = Field(
        title = "select_config",
        description = "Active configuration uid for initial time step "
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

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time "
    )

    # \hline \hline

    # Configuration attributes ---

    uid: str = Field(
        title = "uid",
        description = "Configuration unique identifier "
    )

    description: Optional[str] = Field(
        title = "description",
        description = "Configuration description "
    )

    # 

    # 

    # 

    on_cost: float = Field(
        title = "on_cost",
        description = "Dispatchable device operating cost "
    )

    # 

    # 

    # 

    # 

    in_service_time_ub: float = Field(
        title = "in_service_time_ub",
        description = "Maximum time (hr) to operate/in service "
    )

    in_service_time_lb: float = Field(
        title = "in_service_time_lb",
        description = "Minimum time (hr) to operate/in service "
    )

    down_time_ub: float = Field(
        title = "down_time_ub",
        description = "Maximum (hr) down time "
    )

    down_time_lb: float = Field(
        title = "down_time_lb",
        description = "Minimum (hr) down time "
    )

    # 

    pg_nom_ramp_ub: float = Field(
        title = "pg_nom_ramp_ub",
        description = "Maximum ramp up from operating cond."
    )

    pg_start_ramp_ub: float = Field(
        title = "pg_start_ramp_ub",
        description = "Maximum ramp up from startup cond. "
    )

    pg_down_ramp_ub: float = Field(
        title = "pg_down_ramp_ub",
        description = "Maximum ramp up from shutdown cond. "
    )

    # 

    pg_nom_ramp_lb: float = Field(
        title = "pg_nom_ramp_lb",
        description = "Maximum ramp down from operating cond."
    )

    pg_start_ramp_lb: float = Field(
        title = "pg_start_ramp_lb",
        description = "Maximum ramp down from startup cond. "
    )

    pg_down_ramp_lb: float = Field(
        title = "pg_down_ramp_lb",
        description = "Maximum ramp down from shutdown cond. "
    )

    pg_regulation_down_ub: float = Field(
        title = "pg_regulation_down_ub",
        description = "Maximum regulation down reserve "
    )

    pg_regulation_up_ub: float = Field(
        title = "pg_regulation_up_ub",
        description = "Maximum regulation up reserve "
    )

    pg_spin_ub: float = Field(
        title = "pg_spin_ub",
        description = "Maximum spinning reserve "
    )

    pg_cont_ub: float = Field(
        title = "pg_cont_ub",
        description = "Maximum contingency reserve "
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
        description = "Line charge in susceptance "
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

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    # 

    # 

    reserve_required: float = Field(
        title = "reserve_required",
        description = "Active/Reactive power reserve requirement "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    res_vio_cost: float = Field(
        title = "res_vio_cost",
        description = "Reserve violation cost/penalty "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


# -- Timeseries ----------------------------------------------------------------

class General(BidDSJsonBaseModel):

    # Global time attributes

    time_periods: int = Field(
        title = "time_periods",
        description = "The number of time periods "
    )

    interval_duration: float = Field(
        title = "interval_duration",
        description = "Time duration of the intervals in hours "
    )

    # Global violation attributes

    # Optional attributes


class DispatchableDevices:GeneratingUnits,LoadDemands,andStorageDevices(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Dispatchable device unique identifier "
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

    # \hline \hline

    # Initial status attributes within:

    # \hline \hline

    # Configuration attributes ---

    uid: str = Field(
        title = "uid",
        description = "Configuration unique identifier "
    )

    select_ub: int = Field(
        title = "select_ub",
        description = "Configuration selection upper bound ",
        options = [0, 1]
    )

    select_lb: int = Field(
        title = "select_lb",
        description = "Configuration selection lower bound ",
        options = [0, 1]
    )

    pg_ub: float = Field(
        title = "pg_ub",
        description = "Upper bound of active dispatch "
    )

    pg_lb: float = Field(
        title = "pg_lb",
        description = "Lower bound of active dispatch "
    )

    qg_ub: float = Field(
        title = "qg_ub",
        description = "Upper bound of reactive dispatch "
    )

    qg_lb: float = Field(
        title = "qg_lb",
        description = "Lower bound of reactive dispatch "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


# Output Objects ----------------------------------------------------------------

# ------ Static ----------------------------------------------------------------

class General(BidDSJsonBaseModel):

    # Global time attributes

    # Global violation attributes

    p_vio_cost: float = Field(
        title = "p_vio_cost",
        description = "System violation costs for active power violation "
    )

    q_vio_cost: float = Field(
        title = "q_vio_cost",
        description = "System violation costs for reactive power violation "
    )

    p_bus_vio_cost: float = Field(
        title = "p_bus_vio_cost",
        description = "Bus violation costs for active power violation "
    )

    q_bus_vio_cost: float = Field(
        title = "q_bus_vio_cost",
        description = "Bus violation costs for reactive power violation  "
    )

    v_bus_vio_cost: Optional[float] = Field(
        title = "v_bus_vio_cost",
        description = "Bus violation costs for voltage violation "
    )

    mva_branch_vio_cost: float = Field(
        title = "mva_branch_vio_cost",
        description = "Branch violation costs for thermal violation "
    )

    # Optional attributes

    base_norm_mva: Optional[float] = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
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

    # {\color{red} {\tt con\_loss\_factor}}

    area: str = Field(
        title = "area",
        description = "Bus control area "
    )

    zone: str = Field(
        title = "zone",
        description = "Bus control zone "
    )

    # 

    # Location/Operation information

    base_nom_volt: Optional[float] = Field(
        title = "base_nom_volt",
        description = "Bus nominal voltage "
    )

    type: Optional[String] = Field(
        title = "type",
        description = "Bus type ",
        options = ["PQ", "PV", "Slack", "Not_used"]
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

    state: Optional[str] = Field(
        title = "state",
        description = "Bus state location "
    )

    country: Optional[str] = Field(
        title = "country",
        description = "Bus country location "
    )

    # 


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
        description = "Shunt conductance "
    )

    bs: float = Field(
        title = "bs",
        description = "Shunt susceptance "
    )

    steps_ub: int = Field(
        title = "steps_ub",
        description = "Maximum number of steps "
    )

    steps_lb: int = Field(
        title = "steps_lb",
        description = "Minimum number of steps "
    )


class DispatchableDevices:GeneratingUnits,LoadDemands,andStorageDevices(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Dispatchable device unique identifier "
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
        description = "Dispatchable device startup cost "
    )

    shutdown_cost: float = Field(
        title = "shutdown_cost",
        description = "Dispatchable device shutdown cost "
    )

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

    config_num: int = Field(
        title = "config_num",
        description = "Number of operating modes/configurations "
    )

    # \hline \hline

    # Initial status attributes within:

    on_status_ub: int = Field(
        title = "on_status_ub",
        description = "On status indicator upper bound for initial time step ",
        options = [0, 1]
    )

    on_status_lb: int = Field(
        title = "on_status_lb",
        description = "On status indicator lower bound for initial time step ",
        options = [0, 1]
    )

    select_config: str = Field(
        title = "select_config",
        description = "Active configuration uid for initial time step "
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

    accu_down_time: float = Field(
        title = "accu_down_time",
        description = "Accumulated down time "
    )

    accu_up_time: float = Field(
        title = "accu_up_time",
        description = "Accumulated up time "
    )

    # \hline \hline

    # Configuration attributes ---

    uid: str = Field(
        title = "uid",
        description = "Configuration unique identifier "
    )

    description: Optional[str] = Field(
        title = "description",
        description = "Configuration description "
    )

    # 

    # 

    # 

    on_cost: float = Field(
        title = "on_cost",
        description = "Dispatchable device operating cost "
    )

    # 

    # 

    # 

    # 

    in_service_time_ub: float = Field(
        title = "in_service_time_ub",
        description = "Maximum time (hr) to operate/in service "
    )

    in_service_time_lb: float = Field(
        title = "in_service_time_lb",
        description = "Minimum time (hr) to operate/in service "
    )

    down_time_ub: float = Field(
        title = "down_time_ub",
        description = "Maximum (hr) down time "
    )

    down_time_lb: float = Field(
        title = "down_time_lb",
        description = "Minimum (hr) down time "
    )

    # 

    pg_nom_ramp_ub: float = Field(
        title = "pg_nom_ramp_ub",
        description = "Maximum ramp up from operating cond."
    )

    pg_start_ramp_ub: float = Field(
        title = "pg_start_ramp_ub",
        description = "Maximum ramp up from startup cond. "
    )

    pg_down_ramp_ub: float = Field(
        title = "pg_down_ramp_ub",
        description = "Maximum ramp up from shutdown cond. "
    )

    # 

    pg_nom_ramp_lb: float = Field(
        title = "pg_nom_ramp_lb",
        description = "Maximum ramp down from operating cond."
    )

    pg_start_ramp_lb: float = Field(
        title = "pg_start_ramp_lb",
        description = "Maximum ramp down from startup cond. "
    )

    pg_down_ramp_lb: float = Field(
        title = "pg_down_ramp_lb",
        description = "Maximum ramp down from shutdown cond. "
    )

    pg_regulation_down_ub: float = Field(
        title = "pg_regulation_down_ub",
        description = "Maximum regulation down reserve "
    )

    pg_regulation_up_ub: float = Field(
        title = "pg_regulation_up_ub",
        description = "Maximum regulation up reserve "
    )

    pg_spin_ub: float = Field(
        title = "pg_spin_ub",
        description = "Maximum spinning reserve "
    )

    pg_cont_ub: float = Field(
        title = "pg_cont_ub",
        description = "Maximum contingency reserve "
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
        description = "Line charge in susceptance "
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

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Region reserve unique identifier "
    )

    # 

    # 

    reserve_required: float = Field(
        title = "reserve_required",
        description = "Active/Reactive power reserve requirement "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    res_vio_cost: float = Field(
        title = "res_vio_cost",
        description = "Reserve violation cost/penalty "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


# -- Timeseries ----------------------------------------------------------------

class General(BidDSJsonBaseModel):

    # Global time attributes

    time_periods: int = Field(
        title = "time_periods",
        description = "The number of time periods "
    )

    interval_duration: float = Field(
        title = "interval_duration",
        description = "Time duration of the intervals in hours "
    )

    # Global violation attributes

    # Optional attributes


class DispatchableDevices:GeneratingUnits,LoadDemands,andStorageDevices(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Dispatchable device unique identifier "
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

    # \hline \hline

    # Initial status attributes within:

    # \hline \hline

    # Configuration attributes ---

    uid: str = Field(
        title = "uid",
        description = "Configuration unique identifier "
    )

    select_ub: int = Field(
        title = "select_ub",
        description = "Configuration selection upper bound ",
        options = [0, 1]
    )

    select_lb: int = Field(
        title = "select_lb",
        description = "Configuration selection lower bound ",
        options = [0, 1]
    )

    pg_ub: float = Field(
        title = "pg_ub",
        description = "Upper bound of active dispatch "
    )

    pg_lb: float = Field(
        title = "pg_lb",
        description = "Lower bound of active dispatch "
    )

    qg_ub: float = Field(
        title = "qg_ub",
        description = "Upper bound of reactive dispatch "
    )

    qg_lb: float = Field(
        title = "qg_lb",
        description = "Lower bound of reactive dispatch "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


