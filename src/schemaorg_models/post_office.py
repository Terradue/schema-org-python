from typing import Literal
from pydantic import Field
from schemaorg_models.government_office import GovernmentOffice


class PostOffice(GovernmentOffice):
    """
A post office.
    """
    type_: Literal['https://schema.org/PostOffice'] = Field(default='https://schema.org/PostOffice', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
