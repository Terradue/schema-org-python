from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """
Brewery.
    """
    type_: Literal['https://schema.org/Brewery'] = Field(default='https://schema.org/Brewery', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
