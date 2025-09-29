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

class SheetMusic(CreativeWork):
    '''
    Printed music, as opposed to performed or recorded music.
    '''
    class_: Literal['https://schema.org/SheetMusic'] = Field( # type: ignore
        default='https://schema.org/SheetMusic',
        alias='@type',
        serialization_alias='@type'
    )
