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
from .creative_work_series import CreativeWorkSeries

class BookSeries(CreativeWorkSeries):
    '''
    A series of books. Included books can be indicated with the hasPart property.
    '''
    class_: Literal['https://schema.org/BookSeries'] = Field( # type: ignore
        default='https://schema.org/BookSeries',
        alias='@type',
        serialization_alias='@type'
    )
