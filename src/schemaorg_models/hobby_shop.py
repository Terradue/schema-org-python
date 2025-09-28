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

class HobbyShop(Store):
    """
A store that sells materials useful or necessary for various hobbies.
    """
    class_: Literal['https://schema.org/HobbyShop'] = Field( # type: ignore
        default='https://schema.org/HobbyShop',
        alias='@type',
        serialization_alias='@type'
    )
