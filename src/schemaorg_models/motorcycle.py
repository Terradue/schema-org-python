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

class Motorcycle(Vehicle):
    '''
    A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.
    '''
    class_: Literal['https://schema.org/Motorcycle'] = Field( # type: ignore
        default='https://schema.org/Motorcycle',
        alias='@type',
        serialization_alias='@type'
    )
