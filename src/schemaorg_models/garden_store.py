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

class GardenStore(Store):
    """
A garden store.
    """
    class_: Literal['https://schema.org/GardenStore'] = Field( # type: ignore
        default='https://schema.org/GardenStore',
        alias='@type',
        serialization_alias='@type'
    )
