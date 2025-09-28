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
from .quantitative_value import QuantitativeValue

class SomeProducts(Product):
    """
A placeholder for multiple similar products of the same kind.
    """
    class_: Literal['https://schema.org/SomeProducts'] = Field( # type: ignore
        default='https://schema.org/SomeProducts',
        alias='@type',
        serialization_alias='@type'
    )
    inventoryLevel: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel',
            'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel'
    )
