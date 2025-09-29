from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .digital_document import DigitalDocument

class NoteDigitalDocument(DigitalDocument):
    '''
    A file containing a note, primarily for the author.
    '''
    class_: Literal['https://schema.org/NoteDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/NoteDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
