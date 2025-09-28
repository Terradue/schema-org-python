from __future__ import annotations

from .control_action import ControlAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ActivateAction(ControlAction):
    """
The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).
    """
    class_: Literal['https://schema.org/ActivateAction'] = Field( # type: ignore
        default='https://schema.org/ActivateAction',
        alias='@type',
        serialization_alias='@type'
    )
