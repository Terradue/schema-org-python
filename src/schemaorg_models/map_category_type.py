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

class MapCategoryType(Enumeration):
    '''
    An enumeration of several kinds of Map.
    '''
    class_: Literal['https://schema.org/MapCategoryType'] = Field( # type: ignore
        default='https://schema.org/MapCategoryType',
        alias='@type',
        serialization_alias='@type'
    )
