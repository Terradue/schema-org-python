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

class BikeStore(Store):
    '''
    A bike store.
    '''
    class_: Literal['https://schema.org/BikeStore'] = Field( # type: ignore
        default='https://schema.org/BikeStore',
        alias='@type',
        serialization_alias='@type'
    )
