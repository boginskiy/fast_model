from pydantic import BaseModel
from .Application import DpApplication
from .Antifraud import DpAntifreeze
from .Deals import DpDeals


class Request(BaseModel):
    Application: DpApplication = DpApplication()
    Antifreeze: DpAntifreeze = DpAntifreeze()
    Deals: DpDeals = DpDeals()
