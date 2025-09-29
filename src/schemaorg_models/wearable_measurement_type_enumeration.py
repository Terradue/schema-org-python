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

class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    '''
    Enumerates common types of measurement for wearables products.
    '''
    class_: Literal['https://schema.org/WearableMeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableMeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
