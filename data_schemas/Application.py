from typing import List, Union, Optional
from pydantic import BaseModel, validator, Field
from datetime import datetime
from .default_attr import Default


class DpApplication(BaseModel):
    Start_date: datetime = Default.date_default
    # Принимает значение или None.
    Purpose: List[Optional[int]] = [0] * 5
    # Delta_arr:
    Phone: str = ""
