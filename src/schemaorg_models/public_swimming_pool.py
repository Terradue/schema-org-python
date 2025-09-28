from __future__ import annotations

from .sports_activity_location import SportsActivityLocation    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PublicSwimmingPool(SportsActivityLocation):
    """
A public swimming pool.
    """
    class_: Literal['https://schema.org/PublicSwimmingPool'] = Field( # type: ignore
        default='https://schema.org/PublicSwimmingPool',
        alias='@type',
        serialization_alias='@type'
    )
