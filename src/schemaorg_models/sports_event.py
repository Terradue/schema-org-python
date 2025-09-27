from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.event import Event

from schemaorg_models.person import Person

class SportsEvent(Event):
    """
A sub property of location. The sports event where this action occurred.
    """
    class_: Literal['https://schema.org/SportsEvent'] = Field(default='https://schema.org/SportsEvent', alias='@type', serialization_alias='@type') # type: ignore
    homeTeam: Optional[Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]] = Field(default=None, validation_alias=AliasChoices('homeTeam', 'https://schema.org/homeTeam'), serialization_alias='https://schema.org/homeTeam')
    awayTeam: Optional[Union["SportsTeam", List["SportsTeam"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('awayTeam', 'https://schema.org/awayTeam'), serialization_alias='https://schema.org/awayTeam')
    referee: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('referee', 'https://schema.org/referee'), serialization_alias='https://schema.org/referee')
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('sport', 'https://schema.org/sport'), serialization_alias='https://schema.org/sport')
    @field_serializer('sport')
    def sport2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    competitor: Optional[Union["SportsTeam", List["SportsTeam"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('competitor', 'https://schema.org/competitor'), serialization_alias='https://schema.org/competitor')
