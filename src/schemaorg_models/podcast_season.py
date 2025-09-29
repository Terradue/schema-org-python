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

class PodcastSeason(CreativeWorkSeason):
    '''
    A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.
    '''
    class_: Literal['https://schema.org/PodcastSeason'] = Field( # type: ignore
        default='https://schema.org/PodcastSeason',
        alias='@type',
        serialization_alias='@type'
    )
