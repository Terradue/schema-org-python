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
from .list_item import ListItem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class HowToItem(ListItem):
    """
An item used as either a tool or supply when performing the instructions for how to achieve a result.
    """
    class_: Literal['https://schema.org/HowToItem'] = Field( # type: ignore
        default='https://schema.org/HowToItem',
        alias='@type',
        serialization_alias='@type'
    )
    requiredQuantity: Optional[Union[str, List[str], float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiredQuantity',
            'https://schema.org/requiredQuantity'
        ),
        serialization_alias='https://schema.org/requiredQuantity'
    )
