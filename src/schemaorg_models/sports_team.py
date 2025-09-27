from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.sports_organization import SportsOrganization

from schemaorg_models.person import Person
from schemaorg_models.gender_type import GenderType

class SportsTeam(SportsOrganization):
    """
Organization: Sports team.
    """
    class_: Literal['https://schema.org/SportsTeam'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    athlete: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('athlete', 'https://schema.org/athlete'), serialization_alias='https://schema.org/athlete')
    coach: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('coach', 'https://schema.org/coach'), serialization_alias='https://schema.org/coach')
    gender: Optional[Union[GenderType, List[GenderType], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('gender', 'https://schema.org/gender'), serialization_alias='https://schema.org/gender')
