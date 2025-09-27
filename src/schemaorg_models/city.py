from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class City(AdministrativeArea):
    """
A city or town.
    """
    type_: Literal['https://schema.org/City'] = Field(default='https://schema.org/City', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
