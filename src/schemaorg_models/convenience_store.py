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

class ConvenienceStore(Store):
    '''
    A convenience store.
    '''
    class_: Literal['https://schema.org/ConvenienceStore'] = Field( # type: ignore
        default='https://schema.org/ConvenienceStore',
        alias='@type',
        serialization_alias='@type'
    )
