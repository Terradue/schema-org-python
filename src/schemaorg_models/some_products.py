from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class SomeProducts(Product):
    """
A placeholder for multiple similar products of the same kind.
    """
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('inventoryLevel', 'https://schema.org/inventoryLevel'),serialization_alias='https://schema.org/inventoryLevel')
