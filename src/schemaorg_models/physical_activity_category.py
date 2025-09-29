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

class PhysicalActivityCategory(Enumeration):
    '''
    Categories of physical activity, organized by physiologic classification.
    '''
    class_: Literal['https://schema.org/PhysicalActivityCategory'] = Field( # type: ignore
        default='https://schema.org/PhysicalActivityCategory',
        alias='@type',
        serialization_alias='@type'
    )
