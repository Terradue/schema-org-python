from __future__ import annotations

from .interact_action import InteractAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    class_: Literal['https://schema.org/MarryAction'] = Field( # type: ignore
        default='https://schema.org/MarryAction',
        alias='@type',
        serialization_alias='@type'
    )
