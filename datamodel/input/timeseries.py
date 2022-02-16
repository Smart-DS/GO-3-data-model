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
        description = "Time duration of the intervals in hours "
    )

    # Normalization attributes


class ProducingDevices_SingleModeGeneratingUnits(BidDSJsonBaseModel):

    # Input attributes

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

    cost: List[float] = Field(
        title = "cost",
        description = "Array of generation cost blocks "
    )

    # 

    # 

    # 

    # 

    # 

    # Flags for extra parameters


class ProducingDevices_MultipleModeGeneratingUnits(BidDSJsonBaseModel):

    # Input attributes

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

    # \hline \hline

    # Initial status attributes within:

    # 

    # \hline \hline

    # Flags for extra parameters

    # \hline \hline

    # \end{tabular}

    # \end{center}

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Mode attributes

    # \hline \hline

    # Inner mode attributes ---

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

    cost: List[float] = Field(
        title = "cost",
        description = "Array of generation cost blocks "
    )

    # 

    # 

    # 


class ConsumingDevices_LoadsandDemandResponse(BidDSJsonBaseModel):

    # Input attributes

    uid: str = Field(
        title = "uid",
        description = "Consuming device unique identifier "
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

    connection_status_ub: int = Field(
        title = "connection_status_ub",
        description = "Connection capability  upper bound ",
        options = [0, 1]
    )

    connection_status_lb: int = Field(
        title = "connection_status_lb",
        description = "Connection capability lower bound ",
        options = [0, 1]
    )

    pd_ub: float = Field(
        title = "pd_ub",
        description = "Upper bound of active demand "
    )

    pd_lb: float = Field(
        title = "pd_lb",
        description = "Lower bound of active demand "
    )

    qd_ub: float = Field(
        title = "qd_ub",
        description = "Upper bound of reactive demand "
    )

    qd_lb: float = Field(
        title = "qd_lb",
        description = "Lower bound of reactive demand "
    )

    # 

    cost: List[float] = Field(
        title = "cost",
        description = "Array of demand bids/cost blocks "
    )

    # 

    # 

    # Flags for extra parameters

    # \sout{\tt\color{red} storage\_cap}


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

    RAMPING_RESERVE_UP: float = Field(
        title = "RAMPING_RESERVE_UP",
        description = "Ramping reserve up requirement "
    )

    RAMPING_RESERVE_DOWN: float = Field(
        title = "RAMPING_RESERVE_DOWN",
        description = "Ramping reserve down requirement "
    )

    # 

    # 


