from typing import List, Union, Optional
from pydantic import BaseModel, validator, Field
from datetime import datetime
from .default_attr import Default


class DpApplication(BaseModel):
    Start_date: datetime = Default.date_default
    # Принимает значение или None.
    Purpose: int = 0
    Phone: str = ""
