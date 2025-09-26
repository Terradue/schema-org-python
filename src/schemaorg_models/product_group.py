from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product

from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.product import Product

class ProductGroup(Product):
    """
A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.

While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]]. 
    """
    variesBy: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('variesBy', 'https://schema.org/variesBy'),serialization_alias='https://schema.org/variesBy')
    hasVariant: Optional[Union[Product, List[Product]]] = Field(default=None,validation_alias=AliasChoices('hasVariant', 'https://schema.org/hasVariant'),serialization_alias='https://schema.org/hasVariant')
    productGroupID: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('productGroupID', 'https://schema.org/productGroupID'),serialization_alias='https://schema.org/productGroupID')
