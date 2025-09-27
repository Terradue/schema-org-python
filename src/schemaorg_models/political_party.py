from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class PoliticalParty(Organization):
    """
Organization: Political Party.
    """
    class_: Literal['https://schema.org/PoliticalParty'] = Field(default='https://schema.org/PoliticalParty', alias='@type', serialization_alias='@type') # type: ignore
