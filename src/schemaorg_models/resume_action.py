from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .control_action import ControlAction

class ResumeAction(ControlAction):
    '''
    The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).
    '''
    class_: Literal['https://schema.org/ResumeAction'] = Field( # type: ignore
        default='https://schema.org/ResumeAction',
        alias='@type',
        serialization_alias='@type'
    )
