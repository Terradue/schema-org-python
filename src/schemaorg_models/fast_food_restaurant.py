from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """
A fast-food restaurant.
    """
    type_: Literal['https://schema.org/FastFoodRestaurant'] = Field(default='https://schema.org/FastFoodRestaurant', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
