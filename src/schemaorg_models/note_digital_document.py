from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class NoteDigitalDocument(DigitalDocument):
    """
A file containing a note, primarily for the author.
    """
    class_: Literal['https://schema.org/NoteDigitalDocument'] = Field(default='https://schema.org/NoteDigitalDocument', alias='class', serialization_alias='class') # type: ignore
