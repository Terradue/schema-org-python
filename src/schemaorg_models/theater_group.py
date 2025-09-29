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
from .performing_group import PerformingGroup

class TheaterGroup(PerformingGroup):
    '''
    A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.
    '''
    class_: Literal['https://schema.org/TheaterGroup'] = Field( # type: ignore
        default='https://schema.org/TheaterGroup',
        alias='@type',
        serialization_alias='@type'
    )
