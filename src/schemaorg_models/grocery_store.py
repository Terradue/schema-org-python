from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.store import Store

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GroceryStore(Store):
    """
A grocery store.
    """
    class_: Literal['https://schema.org/GroceryStore'] = Field( # type: ignore
        default='https://schema.org/GroceryStore',
        alias='@type',
        serialization_alias='@type'
    )
