from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """
A distillery.
    """
    class_: Literal['https://schema.org/Distillery'] = Field(default='https://schema.org/Distillery', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
