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

class SuspendAction(ControlAction):
    '''
    The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    '''
    class_: Literal['https://schema.org/SuspendAction'] = Field( # type: ignore
        default='https://schema.org/SuspendAction',
        alias='@type',
        serialization_alias='@type'
    )
