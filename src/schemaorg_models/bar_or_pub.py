from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """
A bar or pub.
    """
    type_: Literal['https://schema.org/BarOrPub'] = Field(default='https://schema.org/BarOrPub', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
