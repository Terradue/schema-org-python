from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Winery(FoodEstablishment):
    """
A winery.
    """
    type_: Literal['https://schema.org/Winery'] = Field(default='https://schema.org/Winery', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
