from __future__ import annotations

from .intangible import Intangible    

from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class ProductReturnPolicy(Intangible):
    """
A ProductReturnPolicy provides information about product return policies associated with an [[Organization]] or [[Product]].
    """
    class_: Literal['https://schema.org/ProductReturnPolicy'] = Field( # type: ignore
        default='https://schema.org/ProductReturnPolicy',
        alias='@type',
        serialization_alias='@type'
    )
    productReturnDays: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productReturnDays',
            'https://schema.org/productReturnDays'
        ),
        serialization_alias='https://schema.org/productReturnDays'
    )
    productReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productReturnLink',
            'https://schema.org/productReturnLink'
        ),
        serialization_alias='https://schema.org/productReturnLink'
    )
