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
from .product import Product
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .product_group import ProductGroup

class ProductModel(Product):
    '''
    A datasheet or vendor specification of a product (in the sense of a prototypical description).

    Attributes:
        predecessorOf: A pointer from a previous, often discontinued variant of the product to its newer variant.
        isVariantOf: Indicates the kind of product that this is a variant of. In the case of [[ProductModel]], this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with [[ProductGroup]], this property can apply to any [[Product]] included in the group.
        successorOf: A pointer from a newer variant of a product  to its previous, often discontinued predecessor.
    '''
    class_: Literal['https://schema.org/ProductModel'] = Field( # type: ignore
        default='https://schema.org/ProductModel',
        alias='@type',
        serialization_alias='@type'
    )
    predecessorOf: Optional[Union['ProductModel', List['ProductModel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'predecessorOf',
            'https://schema.org/predecessorOf'
        ),
        serialization_alias='https://schema.org/predecessorOf'
    )
    isVariantOf: Optional[Union['ProductModel', List['ProductModel'], 'ProductGroup', List['ProductGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isVariantOf',
            'https://schema.org/isVariantOf'
        ),
        serialization_alias='https://schema.org/isVariantOf'
    )
    successorOf: Optional[Union['ProductModel', List['ProductModel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'successorOf',
            'https://schema.org/successorOf'
        ),
        serialization_alias='https://schema.org/successorOf'
    )
