from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """
A bar or pub.
    """
    class_: Literal['https://schema.org/BarOrPub'] = Field('class', alias='class', serialization_alias='class') # type: ignore
