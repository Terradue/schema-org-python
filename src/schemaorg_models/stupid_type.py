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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class StupidType(Thing):
    """
A StupidType for testing.
    """
    class_: Literal['https://schema.org/StupidType'] = Field( # type: ignore
        default='https://schema.org/StupidType',
        alias='@type',
        serialization_alias='@type'
    )
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'stupidProperty',
            'https://schema.org/stupidProperty'
        ),
        serialization_alias='https://schema.org/stupidProperty'
    )
