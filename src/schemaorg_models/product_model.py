from __future__ import annotations

from .product import Product    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class ProductModel(Product):
    """
A datasheet or vendor specification of a product (in the sense of a prototypical description).
    """
    class_: Literal['https://schema.org/ProductModel'] = Field( # type: ignore
        default='https://schema.org/ProductModel',
        alias='@type',
        serialization_alias='@type'
    )
    predecessorOf: Optional[Union["ProductModel", List["ProductModel"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'predecessorOf',
            'https://schema.org/predecessorOf'
        ),
        serialization_alias='https://schema.org/predecessorOf'
    )
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"], "ProductGroup", List["ProductGroup"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isVariantOf',
            'https://schema.org/isVariantOf'
        ),
        serialization_alias='https://schema.org/isVariantOf'
    )
    successorOf: Optional[Union["ProductModel", List["ProductModel"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'successorOf',
            'https://schema.org/successorOf'
        ),
        serialization_alias='https://schema.org/successorOf'
    )
