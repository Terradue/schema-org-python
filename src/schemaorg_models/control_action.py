from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .action import Action

class ControlAction(Action):
    """
An agent controls a device or application.
    """
    class_: Literal['https://schema.org/ControlAction'] = Field( # type: ignore
        default='https://schema.org/ControlAction',
        alias='@type',
        serialization_alias='@type'
    )
