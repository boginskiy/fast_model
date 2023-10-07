from typing import List
from pydantic import BaseModel
from datetime import datetime


class DpAntifreeze(BaseModel):
    Cr_score: List[float] = [0.0] * 3
    Mr_score: List[int] = [0] * 5
