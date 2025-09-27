from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class Country(AdministrativeArea):
    """
A country.
    """
    type_: Literal['https://schema.org/Country'] = Field(default='https://schema.org/Country', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
