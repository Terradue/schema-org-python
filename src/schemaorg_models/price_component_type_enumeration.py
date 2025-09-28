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

class PriceComponentTypeEnumeration(Enumeration):
    """
Enumerates different price components that together make up the total price for an offered product.
    """
    class_: Literal['https://schema.org/PriceComponentTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/PriceComponentTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
