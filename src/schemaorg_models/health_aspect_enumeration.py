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

class HealthAspectEnumeration(Enumeration):
    '''
    HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].
    '''
    class_: Literal['https://schema.org/HealthAspectEnumeration'] = Field( # type: ignore
        default='https://schema.org/HealthAspectEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
