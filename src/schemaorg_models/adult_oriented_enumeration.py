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

class AdultOrientedEnumeration(Enumeration):
    """
Enumeration of considerations that make a product relevant or potentially restricted for adults only.
    """
    class_: Literal['https://schema.org/AdultOrientedEnumeration'] = Field( # type: ignore
        default='https://schema.org/AdultOrientedEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
