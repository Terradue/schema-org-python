from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .vehicle import Vehicle

class MotorizedBicycle(Vehicle):
    '''
    A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.
    '''
    class_: Literal['https://schema.org/MotorizedBicycle'] = Field( # type: ignore
        default='https://schema.org/MotorizedBicycle',
        alias='@type',
        serialization_alias='@type'
    )
