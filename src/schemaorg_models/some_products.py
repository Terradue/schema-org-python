from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class SomeProducts(Product):
    """
A placeholder for multiple similar products of the same kind.
    """
    class_: Literal['https://schema.org/SomeProducts'] = Field(default='https://schema.org/SomeProducts', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('inventoryLevel', 'https://schema.org/inventoryLevel'), serialization_alias='https://schema.org/inventoryLevel')
