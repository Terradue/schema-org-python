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

class MensClothingStore(Store):
    '''
    A men's clothing store.
    '''
    class_: Literal['https://schema.org/MensClothingStore'] = Field( # type: ignore
        default='https://schema.org/MensClothingStore',
        alias='@type',
        serialization_alias='@type'
    )
