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

class ContactPointOption(Enumeration):
    '''
    Enumerated options related to a ContactPoint.
    '''
    class_: Literal['https://schema.org/ContactPointOption'] = Field( # type: ignore
        default='https://schema.org/ContactPointOption',
        alias='@type',
        serialization_alias='@type'
    )
