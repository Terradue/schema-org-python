from typing import Union, List, Optional
from datetime import date, datetime
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class Role(Intangible):
    """
Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.\
\
See also [blog post](https://blog.schema.org/2014/06/16/introducing-role/).
    """
    roleName: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('roleName', 'https://schema.org/roleName'),serialization_alias='https://schema.org/roleName')
    namedPosition: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('namedPosition', 'https://schema.org/namedPosition'),serialization_alias='https://schema.org/namedPosition')
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),serialization_alias='https://schema.org/endDate')
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),serialization_alias='https://schema.org/startDate')
