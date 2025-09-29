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

class MeasurementMethodEnum(Enumeration):
    '''
    Enumeration(s) for use with [[measurementMethod]].
    '''
    class_: Literal['https://schema.org/MeasurementMethodEnum'] = Field( # type: ignore
        default='https://schema.org/MeasurementMethodEnum',
        alias='@type',
        serialization_alias='@type'
    )
