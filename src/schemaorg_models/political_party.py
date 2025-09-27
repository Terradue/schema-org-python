from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class PoliticalParty(Organization):
    """
Organization: Political Party.
    """
    type_: Literal['https://schema.org/PoliticalParty'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PoliticalParty'),serialization_alias='class') # type: ignore
