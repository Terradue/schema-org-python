from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible

class ProductReturnPolicy(Intangible):
    '''
    A ProductReturnPolicy provides information about product return policies associated with an [[Organization]] or [[Product]].

    Attributes:
        productReturnDays: The productReturnDays property indicates the number of days (from purchase) within which relevant product return policy is applicable.
        productReturnLink: Indicates a Web page or service by URL, for product return.
    '''
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
