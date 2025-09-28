from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.size_system_enumeration import SizeSystemEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """
Enumerates common size systems specific for wearable products.
    """
    class_: Literal['https://schema.org/WearableSizeSystemEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableSizeSystemEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
