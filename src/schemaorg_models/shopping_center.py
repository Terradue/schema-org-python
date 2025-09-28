from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.local_business import LocalBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ShoppingCenter(LocalBusiness):
    """
A shopping center or mall.
    """
    class_: Literal['https://schema.org/ShoppingCenter'] = Field( # type: ignore
        default='https://schema.org/ShoppingCenter',
        alias='@type',
        serialization_alias='@type'
    )
