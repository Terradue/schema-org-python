from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.how_to_item import HowToItem

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
from schemaorg_models.monetary_amount import MonetaryAmount

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
