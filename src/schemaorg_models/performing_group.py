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

class PerformingGroup(Organization):
    '''
    A performance group, such as a band, an orchestra, or a circus.
    '''
    class_: Literal['https://schema.org/PerformingGroup'] = Field( # type: ignore
        default='https://schema.org/PerformingGroup',
        alias='@type',
        serialization_alias='@type'
    )
