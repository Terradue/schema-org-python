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

class PriceTypeEnumeration(Enumeration):
    """
Enumerates different price types, for example list price, invoice price, and sale price.
    """
    class_: Literal['https://schema.org/PriceTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/PriceTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
