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
from .intangible import Intangible

class Series(Intangible):
    '''
    A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].
    '''
    class_: Literal['https://schema.org/Series'] = Field( # type: ignore
        default='https://schema.org/Series',
        alias='@type',
        serialization_alias='@type'
    )
