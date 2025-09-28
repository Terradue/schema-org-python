from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .control_action import ControlAction

class ResumeAction(ControlAction):
    """
The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).
    """
    class_: Literal['https://schema.org/ResumeAction'] = Field( # type: ignore
        default='https://schema.org/ResumeAction',
        alias='@type',
        serialization_alias='@type'
    )
