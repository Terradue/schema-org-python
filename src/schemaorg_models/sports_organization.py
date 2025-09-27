from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.organization import Organization


class SportsOrganization(Organization):
    """
Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.
    """
    type_: Literal['https://schema.org/SportsOrganization'] = Field(default='https://schema.org/SportsOrganization', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
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

