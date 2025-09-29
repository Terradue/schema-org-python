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

class OutletStore(Store):
    '''
    An outlet store.
    '''
    class_: Literal['https://schema.org/OutletStore'] = Field( # type: ignore
        default='https://schema.org/OutletStore',
        alias='@type',
        serialization_alias='@type'
    )
