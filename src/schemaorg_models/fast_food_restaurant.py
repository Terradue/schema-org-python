from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """
A fast-food restaurant.
    """
    type_: Literal['https://schema.org/FastFoodRestaurant'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FastFoodRestaurant'),serialization_alias='class') # type: ignore
