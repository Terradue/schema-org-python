from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """
Brewery.
    """
    class_: Literal['https://schema.org/Brewery'] = Field('class', alias='class', serialization_alias='class') # type: ignore
