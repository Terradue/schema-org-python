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

class CertificationStatusEnumeration(Enumeration):
    '''
    Enumerates the different statuses of a Certification (Active and Inactive).
    '''
    class_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field( # type: ignore
        default='https://schema.org/CertificationStatusEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
