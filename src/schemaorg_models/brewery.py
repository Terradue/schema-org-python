from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """
Brewery.
    """
    type_: Literal['https://schema.org/Brewery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Brewery'),serialization_alias='class') # type: ignore
