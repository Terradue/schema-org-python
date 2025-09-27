from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """
A cafe or coffee shop.
    """
    type_: Literal['https://schema.org/CafeOrCoffeeShop'] = Field(default='https://schema.org/CafeOrCoffeeShop', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
