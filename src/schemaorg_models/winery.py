from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Winery(FoodEstablishment):
    """
A winery.
    """
    class_: Literal['https://schema.org/Winery'] = Field('class', alias='class', serialization_alias='class') # type: ignore
