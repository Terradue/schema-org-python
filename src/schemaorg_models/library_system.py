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
from .organization import Organization

class LibrarySystem(Organization):
    '''
    A [[LibrarySystem]] is a collaborative system amongst several libraries.
    '''
    class_: Literal['https://schema.org/LibrarySystem'] = Field( # type: ignore
        default='https://schema.org/LibrarySystem',
        alias='@type',
        serialization_alias='@type'
    )
