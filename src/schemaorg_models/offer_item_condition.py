from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OfferItemCondition(Enumeration):
    """
A list of possible conditions for the item.
    """
    class_: Literal['https://schema.org/OfferItemCondition'] = Field( # type: ignore
        default='https://schema.org/OfferItemCondition',
        alias='@type',
        serialization_alias='@type'
    )
