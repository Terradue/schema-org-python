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

class ResearchOrganization(Organization):
    '''
    A Research Organization (e.g. scientific institute, research company).
    '''
    class_: Literal['https://schema.org/ResearchOrganization'] = Field( # type: ignore
        default='https://schema.org/ResearchOrganization',
        alias='@type',
        serialization_alias='@type'
    )
