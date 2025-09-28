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

class Restaurant(FoodEstablishment):
    """
A restaurant.
    """
    class_: Literal['https://schema.org/Restaurant'] = Field( # type: ignore
        default='https://schema.org/Restaurant',
        alias='@type',
        serialization_alias='@type'
    )
