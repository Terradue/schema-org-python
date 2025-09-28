from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .episode import Episode

class PodcastEpisode(Episode):
    """
A single episode of a podcast series.
    """
    class_: Literal['https://schema.org/PodcastEpisode'] = Field( # type: ignore
        default='https://schema.org/PodcastEpisode',
        alias='@type',
        serialization_alias='@type'
    )
