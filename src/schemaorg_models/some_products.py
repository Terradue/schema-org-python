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

class SomeProducts(Product):
    """
A placeholder for multiple similar products of the same kind.
    """
    class_: Literal['https://schema.org/SomeProducts'] = Field( # type: ignore
        default='https://schema.org/SomeProducts',
        alias='@type',
        serialization_alias='@type'
    )
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel',
            'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel'
    )
