from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Winery(FoodEstablishment):
    """
A winery.
    """
    class_: Literal['https://schema.org/Winery'] = Field(default='https://schema.org/Winery', alias='@type', serialization_alias='@type') # type: ignore
