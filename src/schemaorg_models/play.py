from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .creative_work import CreativeWork

class Play(CreativeWork):
    """
A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading. Note: A performance of a Play would be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].
    """
    class_: Literal['https://schema.org/Play'] = Field( # type: ignore
        default='https://schema.org/Play',
        alias='@type',
        serialization_alias='@type'
    )
