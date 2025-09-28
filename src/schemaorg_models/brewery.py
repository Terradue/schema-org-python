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

class Brewery(FoodEstablishment):
    """
Brewery.
    """
    class_: Literal['https://schema.org/Brewery'] = Field( # type: ignore
        default='https://schema.org/Brewery',
        alias='@type',
        serialization_alias='@type'
    )
