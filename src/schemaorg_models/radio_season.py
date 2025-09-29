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
from .creative_work_season import CreativeWorkSeason

class RadioSeason(CreativeWorkSeason):
    '''
    Season dedicated to radio broadcast and associated online delivery.
    '''
    class_: Literal['https://schema.org/RadioSeason'] = Field( # type: ignore
        default='https://schema.org/RadioSeason',
        alias='@type',
        serialization_alias='@type'
    )
