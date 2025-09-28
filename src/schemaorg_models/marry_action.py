from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .interact_action import InteractAction

class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    class_: Literal['https://schema.org/MarryAction'] = Field( # type: ignore
        default='https://schema.org/MarryAction',
        alias='@type',
        serialization_alias='@type'
    )
