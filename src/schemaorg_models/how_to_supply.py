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
from .monetary_amount import MonetaryAmount
from .how_to_item import HowToItem

class HowToSupply(HowToItem):
    """
A supply consumed when performing the instructions for how to achieve a result.
    """
    class_: Literal['https://schema.org/HowToSupply'] = Field( # type: ignore
        default='https://schema.org/HowToSupply',
        alias='@type',
        serialization_alias='@type'
    )
    estimatedCost: Optional[Union[str, List[str], MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedCost',
            'https://schema.org/estimatedCost'
        ),
        serialization_alias='https://schema.org/estimatedCost'
    )
