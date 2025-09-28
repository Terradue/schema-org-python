from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

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
