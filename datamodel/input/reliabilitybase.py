import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, root_validator, StrictInt, conint, confloat
from pydantic.json import isoformat, timedelta_isoformat
from typing import Dict, List, Optional, Union, Tuple

from datamodel.base import BidDSJsonBaseModel

class ContingencyBase(BidDSJsonBaseModel):

    uid: str = Field(
        title = "uid",
        description = "Contingency unique identifier "
    )

    components: List[str] = Field(
        title = "components",
        description = "A JSON array, where each element is an unique identifier (string) for the contingency component "
    )


