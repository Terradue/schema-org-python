from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.food_establishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """
A bar or pub.
    """
    type_: Literal['https://schema.org/BarOrPub'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BarOrPub'),serialization_alias='class') # type: ignore
