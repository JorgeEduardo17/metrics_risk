# Models
#Python
from datetime import date, datetime, time

#Pydantic
from pydantic import BaseModel
from pydantic import Field

class Log(BaseModel):
    IsUserKnown: bool = Field(
        ...,
        )

    IsClientKnown: bool = Field(
        ...,
        )

    IsIPKnown: bool = Field(
        ...,
        )

    IsIPInternal: bool = Field(
        ...,
        )
    
    LastSuccessfulLoginDate: time = Field(
        ...
        )

    LastFailedLoginDate: time = Field(
        ...
        )

    FailedLoginCountLastWeek: int = Field(
        ...,
        gt=0
    )