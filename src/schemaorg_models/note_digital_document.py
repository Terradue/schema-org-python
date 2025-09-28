from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.digital_document import DigitalDocument

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
