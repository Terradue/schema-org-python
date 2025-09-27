from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.digital_document import DigitalDocument


class NoteDigitalDocument(DigitalDocument):
    """
A file containing a note, primarily for the author.
    """
    type_: Literal['https://schema.org/NoteDigitalDocument'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/NoteDigitalDocument'),serialization_alias='class') # type: ignore
