from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.organization import Organization


class SportsOrganization(Organization):
    """
Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.
    """
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('sport', 'https://schema.org/sport'),serialization_alias='https://schema.org/sport')
    @field_serializer('sport')
    def sport2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

