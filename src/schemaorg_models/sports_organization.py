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

class SportsOrganization(Organization):
    '''
    Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.

    Attributes:
        sport: A type of sport (e.g. Baseball).
    '''
    class_: Literal['https://schema.org/SportsOrganization'] = Field( # type: ignore
        default='https://schema.org/SportsOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sport',
            'https://schema.org/sport'
        ),
        serialization_alias='https://schema.org/sport'
    )
