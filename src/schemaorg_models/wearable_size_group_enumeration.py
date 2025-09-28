from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.size_group_enumeration import SizeGroupEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """
Enumerates common size groups (also known as "size types") for wearable products.
    """
    class_: Literal['https://schema.org/WearableSizeGroupEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableSizeGroupEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
