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
from .episode import Episode

class PodcastEpisode(Episode):
    '''
    A single episode of a podcast series.
    '''
    class_: Literal['https://schema.org/PodcastEpisode'] = Field( # type: ignore
        default='https://schema.org/PodcastEpisode',
        alias='@type',
        serialization_alias='@type'
    )
