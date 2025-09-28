from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .control_action import ControlAction

class DeactivateAction(ControlAction):
    """
The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).
    """
    class_: Literal['https://schema.org/DeactivateAction'] = Field( # type: ignore
        default='https://schema.org/DeactivateAction',
        alias='@type',
        serialization_alias='@type'
    )
