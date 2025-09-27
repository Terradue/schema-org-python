from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """
A distillery.
    """
    type_: Literal['https://schema.org/Distillery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Distillery'),serialization_alias='class') # type: ignore
