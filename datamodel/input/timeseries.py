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

    # 

    # Normalization attributes

    # \end{tabular}

    # \end{center}

    # 


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
        description = "{\color{red} (Case: producer) Upper bound of active dispatch "
    )

    # 

    p_lb: float = Field(
        title = "p_lb",
        description = "{\color{red} (Case: producer) Lower bound of active dispatch "
    )

    # 

    q_ub: float = Field(
        title = "q_ub",
        description = "{\color{red} (Case: producer) Upper bound of reactive dispatch "
    )

    # 

    q_lb: float = Field(
        title = "q_lb",
        description = "{\color{red} (Case: producer) Lower bound of reactive dispatch "
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

    # 

    # 

    # 

    # Reactive cap. attributes

    # 

    # Reactive cap. attributes

    # 

    # 

    # 

    # Storage attributes

    energy_ub: float = Field(
        title = "energy_ub",
        description = "Upper bound for energy storage "
    )

    energy_lb: float = Field(
        title = "energy_lb",
        description = "Lower bound for energy storage "
    )

    pg_ext: float = Field(
        title = "pg_ext",
        description = "External power flow to storage facility "
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

    # 

    # 

    # Flags for extra parameters

    # \end{tabular}

    # \end{center}

    # 

    # \begin{center}

    # \small

    # \begin{tabular}{ l | l | c | c | c |}

    # Initial condition attributes

    # 

    # 

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

    # 

    p_ub: float = Field(
        title = "p_ub",
        description = "{\color{red} (Case: producer) Upper bound of active dispatch "
    )

    # 

    p_lb: float = Field(
        title = "p_lb",
        description = "{\color{red} (Case: producer) Lower bound of active dispatch "
    )

    # 

    q_ub: float = Field(
        title = "q_ub",
        description = "{\color{red} (Case: producer) Upper bound of reactive dispatch "
    )

    # 

    q_lb: float = Field(
        title = "q_lb",
        description = "{\color{red} (Case: producer) Lower bound of reactive dispatch "
    )

    # 

    # 

    # 

    # 

    # 

    # 

    # 

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

    # 

    # \hline \hline

    # Reactive cap.

    # 

    # 

    # Storage attributes

    energy_ub: float = Field(
        title = "energy_ub",
        description = "Upper bound for energy storage "
    )

    energy_lb: float = Field(
        title = "energy_lb",
        description = "Lower bound for energy storage "
    )

    pg_ext: float = Field(
        title = "pg_ext",
        description = "External power flow to storage facility "
    )

    # \end{tabular}

    # \end{center}

    # 

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

    # 

    # 


