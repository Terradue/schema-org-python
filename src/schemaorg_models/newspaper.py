from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .periodical import Periodical

class Newspaper(Periodical):
    """
A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.
    """
    class_: Literal['https://schema.org/Newspaper'] = Field( # type: ignore
        default='https://schema.org/Newspaper',
        alias='@type',
        serialization_alias='@type'
    )
