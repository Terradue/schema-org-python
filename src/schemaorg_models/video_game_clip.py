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

class VideoGameClip(Clip):
    '''
    A short segment/part of a video game.
    '''
    class_: Literal['https://schema.org/VideoGameClip'] = Field( # type: ignore
        default='https://schema.org/VideoGameClip',
        alias='@type',
        serialization_alias='@type'
    )
