from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class ProductCollection(Product):
    """
A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].
    """
    includesObject: Optional[Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]] = Field(default=None,validation_alias=AliasChoices('includesObject', 'https://schema.org/includesObject'),serialization_alias='https://schema.org/includesObject')
