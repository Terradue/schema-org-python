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

class TireShop(Store):
    '''
    A tire shop.
    '''
    class_: Literal['https://schema.org/TireShop'] = Field( # type: ignore
        default='https://schema.org/TireShop',
        alias='@type',
        serialization_alias='@type'
    )
