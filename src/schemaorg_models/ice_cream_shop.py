from typing import Literal
from pydantic import Field
from schemaorg_models.food_establishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """
An ice cream shop.
    """
    class_: Literal['https://schema.org/IceCreamShop'] = Field(default='https://schema.org/IceCreamShop', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
