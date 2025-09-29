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
from .media_object import MediaObject

class MusicVideoObject(MediaObject):
    '''
    A music video file.
    '''
    class_: Literal['https://schema.org/MusicVideoObject'] = Field( # type: ignore
        default='https://schema.org/MusicVideoObject',
        alias='@type',
        serialization_alias='@type'
    )
