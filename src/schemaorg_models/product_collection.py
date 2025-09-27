from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class ProductCollection(Product):
    """
A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].
    """
    class_: Literal['https://schema.org/ProductCollection'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    includesObject: Optional[Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]] = Field(default=None,validation_alias=AliasChoices('includesObject', 'https://schema.org/includesObject'), serialization_alias='https://schema.org/includesObject')
