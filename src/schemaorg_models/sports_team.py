from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .gender_type import GenderType
from .sports_organization import SportsOrganization
from .person import Person

class SportsTeam(SportsOrganization):
    """
Organization: Sports team.
    """
    class_: Literal['https://schema.org/SportsTeam'] = Field( # type: ignore
        default='https://schema.org/SportsTeam',
        alias='@type',
        serialization_alias='@type'
    )
    athlete: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'athlete',
            'https://schema.org/athlete'
        ),
        serialization_alias='https://schema.org/athlete'
    )
    coach: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'coach',
            'https://schema.org/coach'
        ),
        serialization_alias='https://schema.org/coach'
    )
    gender: Optional[Union[GenderType, List[GenderType], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gender',
            'https://schema.org/gender'
        ),
        serialization_alias='https://schema.org/gender'
    )
