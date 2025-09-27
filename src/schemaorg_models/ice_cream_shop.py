from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """
An ice cream shop.
    """
    class_: Literal['https://schema.org/IceCreamShop'] = Field(default='https://schema.org/IceCreamShop', alias='class', serialization_alias='class') # type: ignore
