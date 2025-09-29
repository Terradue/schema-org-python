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
from .enumeration import Enumeration

class BookFormatType(Enumeration):
    '''
    The publication format of the book.
    '''
    class_: Literal['https://schema.org/BookFormatType'] = Field( # type: ignore
        default='https://schema.org/BookFormatType',
        alias='@type',
        serialization_alias='@type'
    )
