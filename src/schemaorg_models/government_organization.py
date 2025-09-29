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

class GovernmentOrganization(Organization):
    '''
    A governmental organization or agency.
    '''
    class_: Literal['https://schema.org/GovernmentOrganization'] = Field( # type: ignore
        default='https://schema.org/GovernmentOrganization',
        alias='@type',
        serialization_alias='@type'
    )
