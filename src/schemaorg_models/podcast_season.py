from __future__ import annotations

from .creative_work_season import CreativeWorkSeason    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PodcastSeason(CreativeWorkSeason):
    """
A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.
    """
    class_: Literal['https://schema.org/PodcastSeason'] = Field( # type: ignore
        default='https://schema.org/PodcastSeason',
        alias='@type',
        serialization_alias='@type'
    )
