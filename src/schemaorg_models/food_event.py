from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.event import Event

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FoodEvent(Event):
    """
A sub property of location. The specific food event where the action occurred.
    """
    class_: Literal['https://schema.org/FoodEvent'] = Field( # type: ignore
        default='https://schema.org/FoodEvent',
        alias='@type',
        serialization_alias='@type'
    )
