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

class ClothingStore(Store):
    '''
    A clothing store.
    '''
    class_: Literal['https://schema.org/ClothingStore'] = Field( # type: ignore
        default='https://schema.org/ClothingStore',
        alias='@type',
        serialization_alias='@type'
    )
