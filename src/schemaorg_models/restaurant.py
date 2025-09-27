from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """
A restaurant.
    """
    class_: Literal['https://schema.org/Restaurant'] = Field(default='https://schema.org/Restaurant', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
