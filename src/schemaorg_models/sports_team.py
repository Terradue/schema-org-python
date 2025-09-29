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
from .sports_organization import SportsOrganization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .gender_type import GenderType

class SportsTeam(SportsOrganization):
    '''
    Organization: Sports team.

    Attributes:
        athlete: A person that acts as performing member of a sports team; a player as opposed to a coach.
        coach: A person that acts in a coaching role for a sports team.
        gender: Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who are not a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed".
    '''
    class_: Literal['https://schema.org/SportsTeam'] = Field( # type: ignore
        default='https://schema.org/SportsTeam',
        alias='@type',
        serialization_alias='@type'
    )
    athlete: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'athlete',
            'https://schema.org/athlete'
        ),
        serialization_alias='https://schema.org/athlete'
    )
    coach: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'coach',
            'https://schema.org/coach'
        ),
        serialization_alias='https://schema.org/coach'
    )
    gender: Optional[Union['GenderType', List['GenderType'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gender',
            'https://schema.org/gender'
        ),
        serialization_alias='https://schema.org/gender'
    )
