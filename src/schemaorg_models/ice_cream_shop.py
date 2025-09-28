from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.food_establishment import FoodEstablishment

from pydantic import (
    Field
)
from typing import (
    Literal
)

class IceCreamShop(FoodEstablishment):
    """
An ice cream shop.
    """
    class_: Literal['https://schema.org/IceCreamShop'] = Field( # type: ignore
        default='https://schema.org/IceCreamShop',
        alias='@type',
        serialization_alias='@type'
    )
