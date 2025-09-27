from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """
An ice cream shop.
    """
    type_: Literal['https://schema.org/IceCreamShop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/IceCreamShop'),serialization_alias='class') # type: ignore
