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

class DeactivateAction(ControlAction):
    '''
    The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).
    '''
    class_: Literal['https://schema.org/DeactivateAction'] = Field( # type: ignore
        default='https://schema.org/DeactivateAction',
        alias='@type',
        serialization_alias='@type'
    )
