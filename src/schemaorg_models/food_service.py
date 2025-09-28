from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .service import Service

class FoodService(Service):
    """
A food service, like breakfast, lunch, or dinner.
    """
    class_: Literal['https://schema.org/FoodService'] = Field( # type: ignore
        default='https://schema.org/FoodService',
        alias='@type',
        serialization_alias='@type'
    )
