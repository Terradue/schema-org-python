from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.product import Product

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
