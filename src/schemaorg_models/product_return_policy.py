from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class ProductReturnPolicy(Intangible):
    """
A ProductReturnPolicy provides information about product return policies associated with an [[Organization]] or [[Product]].
    """
    type_: Literal['https://schema.org/ProductReturnPolicy'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ProductReturnPolicy'),serialization_alias='class') # type: ignore
    productReturnDays: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('productReturnDays', 'https://schema.org/productReturnDays'),serialization_alias='https://schema.org/productReturnDays')
    productReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('productReturnLink', 'https://schema.org/productReturnLink'),serialization_alias='https://schema.org/productReturnLink')
    @field_serializer('productReturnLink')
    def productReturnLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

