# Models
#Python
from datetime import date, datetime, time

#Pydantic
from pydantic import BaseModel
from pydantic import Field



class RegisterFormat(BaseModel):
    date: datetime = Field(
        ...,
        )

    username: str = Field(
        ...,
        )

    mac_address: str = Field(
        ...,
        )

    ip_address: str = Field(
    ...,
    )

    description: str = Field(
    ...,
    )