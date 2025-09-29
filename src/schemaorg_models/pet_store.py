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

class PetStore(Store):
    '''
    A pet store.
    '''
    class_: Literal['https://schema.org/PetStore'] = Field( # type: ignore
        default='https://schema.org/PetStore',
        alias='@type',
        serialization_alias='@type'
    )
