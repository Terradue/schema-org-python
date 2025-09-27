from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """
Brewery.
    """
    type_: Literal['https://schema.org/Brewery'] = Field(default='https://schema.org/Brewery', alias='@type', serialization_alias='@type') # type: ignore
