from __future__ import annotations

from .digital_document import DigitalDocument    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class NoteDigitalDocument(DigitalDocument):
    """
A file containing a note, primarily for the author.
    """
    class_: Literal['https://schema.org/NoteDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/NoteDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
