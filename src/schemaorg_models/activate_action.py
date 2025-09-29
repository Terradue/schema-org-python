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

class ActivateAction(ControlAction):
    '''
    The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).
    '''
    class_: Literal['https://schema.org/ActivateAction'] = Field( # type: ignore
        default='https://schema.org/ActivateAction',
        alias='@type',
        serialization_alias='@type'
    )
