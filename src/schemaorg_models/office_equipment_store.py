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

class OfficeEquipmentStore(Store):
    """
An office equipment store.
    """
    class_: Literal['https://schema.org/OfficeEquipmentStore'] = Field( # type: ignore
        default='https://schema.org/OfficeEquipmentStore',
        alias='@type',
        serialization_alias='@type'
    )
