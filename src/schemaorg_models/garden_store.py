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

class GardenStore(Store):
    '''
    A garden store.
    '''
    class_: Literal['https://schema.org/GardenStore'] = Field( # type: ignore
        default='https://schema.org/GardenStore',
        alias='@type',
        serialization_alias='@type'
    )
