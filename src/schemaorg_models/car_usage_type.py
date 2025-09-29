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
from .enumeration import Enumeration

class CarUsageType(Enumeration):
    '''
    A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    '''
    class_: Literal['https://schema.org/CarUsageType'] = Field( # type: ignore
        default='https://schema.org/CarUsageType',
        alias='@type',
        serialization_alias='@type'
    )
