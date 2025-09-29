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
from .how_to_item import HowToItem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

class HowToSupply(HowToItem):
    '''
    A supply consumed when performing the instructions for how to achieve a result.

    Attributes:
        estimatedCost: The estimated cost of the supply or supplies consumed when performing instructions.
    '''
    class_: Literal['https://schema.org/HowToSupply'] = Field( # type: ignore
        default='https://schema.org/HowToSupply',
        alias='@type',
        serialization_alias='@type'
    )
    estimatedCost: Optional[Union[str, List[str], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
