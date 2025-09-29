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

class JewelryStore(Store):
    '''
    A jewelry store.
    '''
    class_: Literal['https://schema.org/JewelryStore'] = Field( # type: ignore
        default='https://schema.org/JewelryStore',
        alias='@type',
        serialization_alias='@type'
    )
