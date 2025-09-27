from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """
A restaurant.
    """
    class_: Literal['https://schema.org/Restaurant'] = Field(default='https://schema.org/Restaurant', alias='class', serialization_alias='class') # type: ignore
