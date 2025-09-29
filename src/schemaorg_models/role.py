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
from .intangible import Intangible

class Role(Intangible):
    '''
    Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.\
\
See also [blog post](https://blog.schema.org/2014/06/16/introducing-role/).

    Attributes:
        roleName: A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'.
        namedPosition: A position played, performed or filled by a person or organization, as part of an organization. For example, an athlete in a SportsTeam might play in the position named 'Quarterback'.
        endDate: The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        startDate: The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    '''
    class_: Literal['https://schema.org/Role'] = Field( # type: ignore
        default='https://schema.org/Role',
        alias='@type',
        serialization_alias='@type'
    )
    roleName: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    namedPosition: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
