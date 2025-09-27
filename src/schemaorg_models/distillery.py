from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """
A distillery.
    """
    type_: Literal['https://schema.org/Distillery'] = Field(default='https://schema.org/Distillery', alias='@type', serialization_alias='@type') # type: ignore
