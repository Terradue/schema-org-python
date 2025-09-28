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

class IndividualProduct(Product):
    """
A single, identifiable product instance (e.g. a laptop with a particular serial number).
    """
    class_: Literal['https://schema.org/IndividualProduct'] = Field( # type: ignore
        default='https://schema.org/IndividualProduct',
        alias='@type',
        serialization_alias='@type'
    )
    serialNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serialNumber',
            'https://schema.org/serialNumber'
        ),
        serialization_alias='https://schema.org/serialNumber'
    )
