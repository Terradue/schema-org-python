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
from .clip import Clip

class MovieClip(Clip):
    '''
    A short segment/part of a movie.
    '''
    class_: Literal['https://schema.org/MovieClip'] = Field( # type: ignore
        default='https://schema.org/MovieClip',
        alias='@type',
        serialization_alias='@type'
    )
