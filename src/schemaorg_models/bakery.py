from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """
A bakery.
    """
    type_: Literal['https://schema.org/Bakery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Bakery'),serialization_alias='class') # type: ignore
