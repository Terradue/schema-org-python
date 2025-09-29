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

class TextObject(MediaObject):
    '''
    A text file. The text can be unformatted or contain markup, html, etc.
    '''
    class_: Literal['https://schema.org/TextObject'] = Field( # type: ignore
        default='https://schema.org/TextObject',
        alias='@type',
        serialization_alias='@type'
    )
