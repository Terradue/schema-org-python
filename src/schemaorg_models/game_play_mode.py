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
from .enumeration import Enumeration

class GamePlayMode(Enumeration):
    '''
    Indicates whether this game is multi-player, co-op or single-player.
    '''
    class_: Literal['https://schema.org/GamePlayMode'] = Field( # type: ignore
        default='https://schema.org/GamePlayMode',
        alias='@type',
        serialization_alias='@type'
    )
