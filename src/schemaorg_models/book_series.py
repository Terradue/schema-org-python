from __future__ import annotations

from .creative_work_series import CreativeWorkSeries    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BookSeries(CreativeWorkSeries):
    """
A series of books. Included books can be indicated with the hasPart property.
    """
    class_: Literal['https://schema.org/BookSeries'] = Field( # type: ignore
        default='https://schema.org/BookSeries',
        alias='@type',
        serialization_alias='@type'
    )
