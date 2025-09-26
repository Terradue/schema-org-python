from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.organization import Organization


class SportsOrganization(Organization):
    """
Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.
    """
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('sport', 'https://schema.org/sport'),serialization_alias='https://schema.org/sport')
