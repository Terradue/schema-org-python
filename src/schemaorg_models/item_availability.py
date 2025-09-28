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

class ItemAvailability(Enumeration):
    """
A list of possible product availability options.
    """
    class_: Literal['https://schema.org/ItemAvailability'] = Field( # type: ignore
        default='https://schema.org/ItemAvailability',
        alias='@type',
        serialization_alias='@type'
    )
