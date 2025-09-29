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
from .store import Store

class GroceryStore(Store):
    '''
    A grocery store.
    '''
    class_: Literal['https://schema.org/GroceryStore'] = Field( # type: ignore
        default='https://schema.org/GroceryStore',
        alias='@type',
        serialization_alias='@type'
    )
