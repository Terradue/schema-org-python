from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BookFormatType(Enumeration):
    """
The publication format of the book.
    """
    class_: Literal['https://schema.org/BookFormatType'] = Field( # type: ignore
        default='https://schema.org/BookFormatType',
        alias='@type',
        serialization_alias='@type'
    )
