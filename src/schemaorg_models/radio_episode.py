from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .episode import Episode

class RadioEpisode(Episode):
    """
A radio episode which can be part of a series or season.
    """
    class_: Literal['https://schema.org/RadioEpisode'] = Field( # type: ignore
        default='https://schema.org/RadioEpisode',
        alias='@type',
        serialization_alias='@type'
    )
