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

class PawnShop(Store):
    """
A shop that will buy, or lend money against the security of, personal possessions.
    """
    class_: Literal['https://schema.org/PawnShop'] = Field( # type: ignore
        default='https://schema.org/PawnShop',
        alias='@type',
        serialization_alias='@type'
    )
