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
from .enumeration import Enumeration

class LegalValueLevel(Enumeration):
    '''
    A list of possible levels for the legal validity of a legislation.
    '''
    class_: Literal['https://schema.org/LegalValueLevel'] = Field( # type: ignore
        default='https://schema.org/LegalValueLevel',
        alias='@type',
        serialization_alias='@type'
    )
