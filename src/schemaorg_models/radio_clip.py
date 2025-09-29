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

class RadioClip(Clip):
    '''
    A short radio program or a segment/part of a radio program.
    '''
    class_: Literal['https://schema.org/RadioClip'] = Field( # type: ignore
        default='https://schema.org/RadioClip',
        alias='@type',
        serialization_alias='@type'
    )
