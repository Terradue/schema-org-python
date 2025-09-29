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

class AutoPartsStore(Store):
    '''
    An auto parts store.
    '''
    class_: Literal['https://schema.org/AutoPartsStore'] = Field( # type: ignore
        default='https://schema.org/AutoPartsStore',
        alias='@type',
        serialization_alias='@type'
    )
