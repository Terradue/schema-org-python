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

class TextDigitalDocument(DigitalDocument):
    '''
    A file composed primarily of text.
    '''
    class_: Literal['https://schema.org/TextDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/TextDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
