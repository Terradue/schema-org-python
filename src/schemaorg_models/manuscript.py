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
from .creative_work import CreativeWork

class Manuscript(CreativeWork):
    '''
    A book, document, or piece of music written by hand rather than typed or printed.
    '''
    class_: Literal['https://schema.org/Manuscript'] = Field( # type: ignore
        default='https://schema.org/Manuscript',
        alias='@type',
        serialization_alias='@type'
    )
