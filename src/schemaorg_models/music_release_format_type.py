from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MusicReleaseFormatType(Enumeration):
    """
Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
    """
    class_: Literal['https://schema.org/MusicReleaseFormatType'] = Field( # type: ignore
        default='https://schema.org/MusicReleaseFormatType',
        alias='@type',
        serialization_alias='@type'
    )
