from __future__ import annotations

from .digital_document import DigitalDocument    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TextDigitalDocument(DigitalDocument):
    """
A file composed primarily of text.
    """
    class_: Literal['https://schema.org/TextDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/TextDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
