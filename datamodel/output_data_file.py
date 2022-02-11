
import logging
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import isoformat, timedelta_isoformat
from typing import String, Dict, List, Optional, Union

from .base import BidDSJsonBaseModel

        