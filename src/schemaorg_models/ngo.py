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

class NGO(Organization):
    '''
    Organization: Non-governmental Organization.
    '''
    class_: Literal['https://schema.org/NGO'] = Field( # type: ignore
        default='https://schema.org/NGO',
        alias='@type',
        serialization_alias='@type'
    )
