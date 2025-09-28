from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ShortStory(CreativeWork):
    """
Short story or tale. A brief work of literature, usually written in narrative prose.
    """
    class_: Literal['https://schema.org/ShortStory'] = Field( # type: ignore
        default='https://schema.org/ShortStory',
        alias='@type',
        serialization_alias='@type'
    )
