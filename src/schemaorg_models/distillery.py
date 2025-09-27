from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """
A distillery.
    """
    class_: Literal['https://schema.org/Distillery'] = Field('class', alias='class', serialization_alias='class') # type: ignore
