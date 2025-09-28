from __future__ import annotations
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
from .product import Product
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .type_and_quantity_node import TypeAndQuantityNode

class ProductCollection(Product):
    """
A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].
    """
    class_: Literal['https://schema.org/ProductCollection'] = Field( # type: ignore
        default='https://schema.org/ProductCollection',
        alias='@type',
        serialization_alias='@type'
    )
    includesObject: Optional[Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesObject',
            'https://schema.org/includesObject'
        ),
        serialization_alias='https://schema.org/includesObject'
    )
