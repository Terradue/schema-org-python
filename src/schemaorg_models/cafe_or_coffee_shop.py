from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """
A cafe or coffee shop.
    """
    class_: Literal['https://schema.org/CafeOrCoffeeShop'] = Field(default='https://schema.org/CafeOrCoffeeShop', alias='class', serialization_alias='class') # type: ignore
