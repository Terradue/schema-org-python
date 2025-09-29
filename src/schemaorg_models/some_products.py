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
    from .quantitative_value import QuantitativeValue

class SomeProducts(Product):
    '''
    A placeholder for multiple similar products of the same kind.

    Attributes:
        inventoryLevel: The current approximate inventory level for the item or items.
    '''
    class_: Literal['https://schema.org/SomeProducts'] = Field( # type: ignore
        default='https://schema.org/SomeProducts',
        alias='@type',
        serialization_alias='@type'
    )
    inventoryLevel: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel',
            'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel'
    )
