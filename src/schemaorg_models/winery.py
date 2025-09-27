from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class Winery(FoodEstablishment):
    """
A winery.
    """
    type_: Literal['https://schema.org/Winery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Winery'),serialization_alias='class') # type: ignore
