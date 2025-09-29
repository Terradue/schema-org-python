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

class BookStore(Store):
    '''
    A bookstore.
    '''
    class_: Literal['https://schema.org/BookStore'] = Field( # type: ignore
        default='https://schema.org/BookStore',
        alias='@type',
        serialization_alias='@type'
    )
