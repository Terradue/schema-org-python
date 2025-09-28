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

class ReturnFeesEnumeration(Enumeration):
    """
Enumerates several kinds of policies for product return fees.
    """
    class_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnFeesEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
