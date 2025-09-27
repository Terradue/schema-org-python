from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """
A restaurant.
    """
    type_: Literal['https://schema.org/Restaurant'] = Field(default='https://schema.org/Restaurant', alias='@type', serialization_alias='@type') # type: ignore
