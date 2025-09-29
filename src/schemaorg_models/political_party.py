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

class PoliticalParty(Organization):
    '''
    Organization: Political Party.
    '''
    class_: Literal['https://schema.org/PoliticalParty'] = Field( # type: ignore
        default='https://schema.org/PoliticalParty',
        alias='@type',
        serialization_alias='@type'
    )
