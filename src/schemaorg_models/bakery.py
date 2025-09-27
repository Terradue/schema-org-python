from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """
A bakery.
    """
    class_: Literal['https://schema.org/Bakery'] = Field('class', alias='class', serialization_alias='class') # type: ignore
