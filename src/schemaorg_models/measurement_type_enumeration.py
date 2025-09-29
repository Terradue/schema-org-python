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

class MeasurementTypeEnumeration(Enumeration):
    '''
    Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.
    '''
    class_: Literal['https://schema.org/MeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/MeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
