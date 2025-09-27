from typing import Literal
from pydantic import Field
from schemaorg_models.administrative_area import AdministrativeArea


class State(AdministrativeArea):
    """
A state or province of a country.
    """
    type_: Literal['https://schema.org/State'] = Field(default='https://schema.org/State', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
