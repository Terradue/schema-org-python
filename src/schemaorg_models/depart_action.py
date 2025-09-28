from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .move_action import MoveAction

class DepartAction(MoveAction):
    """
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.
    """
    class_: Literal['https://schema.org/DepartAction'] = Field( # type: ignore
        default='https://schema.org/DepartAction',
        alias='@type',
        serialization_alias='@type'
    )
