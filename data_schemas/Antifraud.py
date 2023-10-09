from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class DpAntifraud(BaseModel):
    Cr_score: List[float] = [0.0] * 3
    Mr_score: List[int] = [0] * 5
