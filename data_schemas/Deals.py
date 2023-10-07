from typing import List
from pydantic import BaseModel
from datetime import datetime
from .default_attr import Default


class DpDeals(BaseModel):
    Start_deal: datetime = Default.date_default
    Status_deal: List[str] = [""] * 10
