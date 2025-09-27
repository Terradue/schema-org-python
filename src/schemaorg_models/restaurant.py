from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """
A restaurant.
    """
    type_: Literal['https://schema.org/Restaurant'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Restaurant'),serialization_alias='class') # type: ignore
