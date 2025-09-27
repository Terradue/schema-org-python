from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class SomeProducts(Product):
    """
A placeholder for multiple similar products of the same kind.
    """
    type_: Literal['https://schema.org/SomeProducts'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SomeProducts'),serialization_alias='class') # type: ignore
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('inventoryLevel', 'https://schema.org/inventoryLevel'),serialization_alias='https://schema.org/inventoryLevel')
