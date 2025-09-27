from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """
A fast-food restaurant.
    """
    class_: Literal['https://schema.org/FastFoodRestaurant'] = Field('class', alias='class', serialization_alias='class') # type: ignore
