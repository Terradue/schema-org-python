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

class AmpStory(MediaObject):
    '''
    A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    '''
    class_: Literal['https://schema.org/AmpStory'] = Field( # type: ignore
        default='https://schema.org/AmpStory',
        alias='@type',
        serialization_alias='@type'
    )
