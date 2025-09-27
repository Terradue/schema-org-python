from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class PoliticalParty(Organization):
    """
Organization: Political Party.
    """
    class_: Literal['https://schema.org/PoliticalParty'] = Field('class', alias='class', serialization_alias='class') # type: ignore
