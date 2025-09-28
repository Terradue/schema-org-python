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

class SizeSystemEnumeration(Enumeration):
    """
Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.
    """
    class_: Literal['https://schema.org/SizeSystemEnumeration'] = Field( # type: ignore
        default='https://schema.org/SizeSystemEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
