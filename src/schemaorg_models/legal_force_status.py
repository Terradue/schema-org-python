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
from .status_enumeration import StatusEnumeration

class LegalForceStatus(StatusEnumeration):
    '''
    A list of possible statuses for the legal force of a legislation.
    '''
    class_: Literal['https://schema.org/LegalForceStatus'] = Field( # type: ignore
        default='https://schema.org/LegalForceStatus',
        alias='@type',
        serialization_alias='@type'
    )
