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

class PresentationDigitalDocument(DigitalDocument):
    '''
    A file containing slides or used for a presentation.
    '''
    class_: Literal['https://schema.org/PresentationDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/PresentationDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
