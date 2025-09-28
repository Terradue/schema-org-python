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

class ShoeStore(Store):
    """
A shoe store.
    """
    class_: Literal['https://schema.org/ShoeStore'] = Field( # type: ignore
        default='https://schema.org/ShoeStore',
        alias='@type',
        serialization_alias='@type'
    )
