from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class ProductReturnPolicy(Intangible):
    """
A ProductReturnPolicy provides information about product return policies associated with an [[Organization]] or [[Product]].
    """
    productReturnDays: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('productReturnDays', 'https://schema.org/productReturnDays'),serialization_alias='https://schema.org/productReturnDays')
    productReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('productReturnLink', 'https://schema.org/productReturnLink'),serialization_alias='https://schema.org/productReturnLink')
    @field_serializer('productReturnLink')
    def productReturnLink2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

