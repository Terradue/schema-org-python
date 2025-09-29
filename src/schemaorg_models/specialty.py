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

class Specialty(Enumeration):
    '''
    Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.
    '''
    class_: Literal['https://schema.org/Specialty'] = Field( # type: ignore
        default='https://schema.org/Specialty',
        alias='@type',
        serialization_alias='@type'
    )
