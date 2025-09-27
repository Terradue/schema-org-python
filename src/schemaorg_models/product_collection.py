from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class ProductCollection(Product):
    """
A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].
    """
    type_: Literal['https://schema.org/ProductCollection'] = Field(default='https://schema.org/ProductCollection', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    includesObject: Optional[Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]] = Field(default=None, validation_alias=AliasChoices('includesObject', 'https://schema.org/includesObject'), serialization_alias='https://schema.org/includesObject')
