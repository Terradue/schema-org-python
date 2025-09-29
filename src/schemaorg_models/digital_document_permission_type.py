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

class DigitalDocumentPermissionType(Enumeration):
    '''
    A type of permission which can be granted for accessing a digital document.
    '''
    class_: Literal['https://schema.org/DigitalDocumentPermissionType'] = Field( # type: ignore
        default='https://schema.org/DigitalDocumentPermissionType',
        alias='@type',
        serialization_alias='@type'
    )
