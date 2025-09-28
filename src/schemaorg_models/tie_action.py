from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .achieve_action import AchieveAction

class TieAction(AchieveAction):
    """
The act of reaching a draw in a competitive activity.
    """
    class_: Literal['https://schema.org/TieAction'] = Field( # type: ignore
        default='https://schema.org/TieAction',
        alias='@type',
        serialization_alias='@type'
    )
