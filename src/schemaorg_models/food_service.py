from __future__ import annotations

from .service import Service    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FoodService(Service):
    """
A food service, like breakfast, lunch, or dinner.
    """
    class_: Literal['https://schema.org/FoodService'] = Field( # type: ignore
        default='https://schema.org/FoodService',
        alias='@type',
        serialization_alias='@type'
    )
