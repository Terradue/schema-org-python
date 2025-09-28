from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.automotive_business import AutomotiveBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutoBodyShop(AutomotiveBusiness):
    """
Auto body shop.
    """
    class_: Literal['https://schema.org/AutoBodyShop'] = Field( # type: ignore
        default='https://schema.org/AutoBodyShop',
        alias='@type',
        serialization_alias='@type'
    )
