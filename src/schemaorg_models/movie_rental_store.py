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

class MovieRentalStore(Store):
    '''
    A movie rental store.
    '''
    class_: Literal['https://schema.org/MovieRentalStore'] = Field( # type: ignore
        default='https://schema.org/MovieRentalStore',
        alias='@type',
        serialization_alias='@type'
    )
