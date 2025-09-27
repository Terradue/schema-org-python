from typing import Literal
from pydantic import Field
from schemaorg_models.landform import Landform


class Continent(Landform):
    """
One of the continents (for example, Europe or Africa).
    """
    type_: Literal['https://schema.org/Continent'] = Field(default='https://schema.org/Continent', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
