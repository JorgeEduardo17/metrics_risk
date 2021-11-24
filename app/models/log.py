#Python
from datetime import date, datetime, time

#Pydantic
from pydantic import BaseModel, Field


class Log(BaseModel):

    date: datetime = Field(
        ...
    )

    username: str = Field(
        min_length=1,
        max_length=20
    )

    ip_address: str = Field(
        min_length=1,
        max_length=20
    )

    mac_address: str = Field(
        min_length=1,
        max_length=20
    )

    description: str = Field(
    ...,
    )

"""     IsUserKnown: bool = Field(
        ...,
        description="Is the user ever log in seen"
        )

    IsClientKnown: bool = Field(
        ...,
        description="Is the computer ever seen before"
        )

    IsIPKnown: bool = Field(
        ...,
        description="Is the connecting ip ever seen before"
        )

    IsIPInternal: bool = Field(
        ...,
        description="Is the connecting ip internal or external"
        )
    
    LastSuccessfulLoginDate: time = Field(
        ...,
        description="Last successful login date for given user"
        )

    LastFailedLoginDate: time = Field(
        ...,
        description="Last failed login date for given user"
        )

    FailedLoginCountLastWeek: int = Field(
        ...,
        description="Number of failed logins for last week"
    ) """