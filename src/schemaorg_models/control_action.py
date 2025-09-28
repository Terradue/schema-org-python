from __future__ import annotations

from .action import Action    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ControlAction(Action):
    """
An agent controls a device or application.
    """
    class_: Literal['https://schema.org/ControlAction'] = Field( # type: ignore
        default='https://schema.org/ControlAction',
        alias='@type',
        serialization_alias='@type'
    )
