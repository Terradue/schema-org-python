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
from .creative_work import CreativeWork

class ShortStory(CreativeWork):
    '''
    Short story or tale. A brief work of literature, usually written in narrative prose.
    '''
    class_: Literal['https://schema.org/ShortStory'] = Field( # type: ignore
        default='https://schema.org/ShortStory',
        alias='@type',
        serialization_alias='@type'
    )
