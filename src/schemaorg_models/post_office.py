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
from .government_office import GovernmentOffice

class PostOffice(GovernmentOffice):
    '''
    A post office.
    '''
    class_: Literal['https://schema.org/PostOffice'] = Field( # type: ignore
        default='https://schema.org/PostOffice',
        alias='@type',
        serialization_alias='@type'
    )
