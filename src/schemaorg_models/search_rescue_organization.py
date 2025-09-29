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

class SearchRescueOrganization(Organization):
    '''
    A Search and Rescue organization of some kind.
    '''
    class_: Literal['https://schema.org/SearchRescueOrganization'] = Field( # type: ignore
        default='https://schema.org/SearchRescueOrganization',
        alias='@type',
        serialization_alias='@type'
    )
