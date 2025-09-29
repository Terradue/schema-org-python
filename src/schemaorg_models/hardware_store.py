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

class HardwareStore(Store):
    '''
    A hardware store.
    '''
    class_: Literal['https://schema.org/HardwareStore'] = Field( # type: ignore
        default='https://schema.org/HardwareStore',
        alias='@type',
        serialization_alias='@type'
    )
