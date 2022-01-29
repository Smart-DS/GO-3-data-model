# Input Objects ----------------------------------------------------------------

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

    v_bus_vio_cost: float = Field(
        title = "v_bus_vio_cost",
        description = "Bus violation costs for voltage violation "
    )

    mva_branch_vio_cost: float = Field(
        title = "mva_branch_vio_cost",
        description = "Branch violation costs for thermal violation "
    )

    # Optional attributes

    base_norm_mva: float = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
    )


class ACTransmissionLine(BidDSJsonBaseModel):

    # Input attributes

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

    # Additional shunt attributes


class TwoWindingTransformer(BidDSJsonBaseModel):

    # Input attributes

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

    # Additional shunt attributes


class DCLine(BidDSJsonBaseModel):

    # Input attributes

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

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


# Output Objects ----------------------------------------------------------------

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

    v_bus_vio_cost: float = Field(
        title = "v_bus_vio_cost",
        description = "Bus violation costs for voltage violation "
    )

    mva_branch_vio_cost: float = Field(
        title = "mva_branch_vio_cost",
        description = "Branch violation costs for thermal violation "
    )

    # Optional attributes

    base_norm_mva: float = Field(
        title = "base_norm_mva",
        description = "Base MVA normalization constant "
    )


class ACTransmissionLine(BidDSJsonBaseModel):

    # Input attributes

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

    # Additional shunt attributes


class TwoWindingTransformer(BidDSJsonBaseModel):

    # Input attributes

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

    # Additional shunt attributes


class DCLine(BidDSJsonBaseModel):

    # Input attributes

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

    # 

    # 

    # 

    # 

    # 

    # 

    # 

    # 


