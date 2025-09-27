from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class NGO(Organization):
    """
Organization: Non-governmental Organization.
    """
    type_: Literal['https://schema.org/NGO'] = Field(default='https://schema.org/NGO', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
