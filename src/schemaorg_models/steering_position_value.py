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
from .qualitative_value import QualitativeValue

class SteeringPositionValue(QualitativeValue):
    '''
    A value indicating a steering position.
    '''
    class_: Literal['https://schema.org/SteeringPositionValue'] = Field( # type: ignore
        default='https://schema.org/SteeringPositionValue',
        alias='@type',
        serialization_alias='@type'
    )
