from typing import List

from pydantic import BaseModel
from .Application import DpApplication
from .Antifraud import DpAntifraud
from .Deals import DpDeals


class Request(BaseModel):
    Application: DpApplication = DpApplication()
    Antifraud: DpAntifraud = DpAntifraud()
    Deals: DpDeals = DpDeals()


class User(BaseModel):
    id: int
    name: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    video: UploadVideo


class Message(BaseModel):
    message: str

