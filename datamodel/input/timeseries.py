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

    interval_duration: float = Field(
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

    startup_status_ub: int = Field(
        title = "startup_status_ub",
        description = "Startup procedure/status upper bound ",
        options = [0, 1]
    )

    startup_status_lb: int = Field(
        title = "startup_status_lb",
        description = "Startup procedure/status lower bound ",
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

    startup_status_ub: int = Field(
        title = "startup_status_ub",
        description = "Startup procedure/status upper bound ",
        options = [0, 1]
    )

    startup_status_lb: int = Field(
        title = "startup_status_lb",
        description = "Startup procedure/status lower bound ",
        options = [0, 1]
    )

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


