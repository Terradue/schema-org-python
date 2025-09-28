from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class OfficeEquipmentStore(Store):
    """
An office equipment store.
    """
    class_: Literal['https://schema.org/OfficeEquipmentStore'] = Field( # type: ignore
        default='https://schema.org/OfficeEquipmentStore',
        alias='@type',
        serialization_alias='@type'
    )
