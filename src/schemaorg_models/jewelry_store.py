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

class JewelryStore(Store):
    """
A jewelry store.
    """
    class_: Literal['https://schema.org/JewelryStore'] = Field( # type: ignore
        default='https://schema.org/JewelryStore',
        alias='@type',
        serialization_alias='@type'
    )
