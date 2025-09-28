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

class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    class_: Literal['https://schema.org/WarrantyScope'] = Field( # type: ignore
        default='https://schema.org/WarrantyScope',
        alias='@type',
        serialization_alias='@type'
    )
