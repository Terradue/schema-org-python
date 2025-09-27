from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """
A cafe or coffee shop.
    """
    type_: Literal['https://schema.org/CafeOrCoffeeShop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CafeOrCoffeeShop'),serialization_alias='class') # type: ignore
