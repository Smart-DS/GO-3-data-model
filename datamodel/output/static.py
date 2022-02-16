import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union

from datamodel.base import BidDSJsonBaseModel

class ProducingDevices_SingleModeGeneratingUnits(BidDSJsonBaseModel):

    # Output attributes

    uid: str = Field(
        title = "uid",
        description = "Device unique identifier "
    )

    pg_flexi_up_online: float = Field(
        title = "pg_flexi_up_online",
        description = "Flexible ramp up reserve when online "
    )

    pg_flexi_down_online: float = Field(
        title = "pg_flexi_down_online",
        description = "Flexible ramp down reserve when online "
    )

    pg_flexi_up_offline: float = Field(
        title = "pg_flexi_up_offline",
        description = "Flexible ramp up reserve when offline "
    )

    pg_flexi_down_offline: float = Field(
        title = "pg_flexi_down_offline",
        description = "Flexible ramp down reserve when offline "
    )


