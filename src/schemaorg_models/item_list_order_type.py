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

class ItemListOrderType(Enumeration):
    """
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
    class_: Literal['https://schema.org/ItemListOrderType'] = Field( # type: ignore
        default='https://schema.org/ItemListOrderType',
        alias='@type',
        serialization_alias='@type'
    )
