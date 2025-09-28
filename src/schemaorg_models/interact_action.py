from __future__ import annotations

from .action import Action    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class InteractAction(Action):
    """
The act of interacting with another person or organization.
    """
    class_: Literal['https://schema.org/InteractAction'] = Field( # type: ignore
        default='https://schema.org/InteractAction',
        alias='@type',
        serialization_alias='@type'
    )
