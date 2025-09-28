from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.move_action import MoveAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DepartAction(MoveAction):
    """
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.
    """
    class_: Literal['https://schema.org/DepartAction'] = Field( # type: ignore
        default='https://schema.org/DepartAction',
        alias='@type',
        serialization_alias='@type'
    )
