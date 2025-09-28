from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Poster(CreativeWork):
    """
A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.
    """
    class_: Literal['https://schema.org/Poster'] = Field( # type: ignore
        default='https://schema.org/Poster',
        alias='@type',
        serialization_alias='@type'
    )
