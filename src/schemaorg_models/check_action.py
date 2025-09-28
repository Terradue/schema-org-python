from __future__ import annotations

from .find_action import FindAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CheckAction(FindAction):
    """
An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.
    """
    class_: Literal['https://schema.org/CheckAction'] = Field( # type: ignore
        default='https://schema.org/CheckAction',
        alias='@type',
        serialization_alias='@type'
    )
