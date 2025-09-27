from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """
A bakery.
    """
    type_: Literal['https://schema.org/Bakery'] = Field(default='https://schema.org/Bakery', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
