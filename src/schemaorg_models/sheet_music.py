from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SheetMusic(CreativeWork):
    """
Printed music, as opposed to performed or recorded music.
    """
    class_: Literal['https://schema.org/SheetMusic'] = Field( # type: ignore
        default='https://schema.org/SheetMusic',
        alias='@type',
        serialization_alias='@type'
    )
