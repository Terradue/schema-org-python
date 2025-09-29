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
from .measurement_type_enumeration import MeasurementTypeEnumeration

class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    '''
    Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.
    '''
    class_: Literal['https://schema.org/BodyMeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/BodyMeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
