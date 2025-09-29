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
from .move_action import MoveAction

class ArriveAction(MoveAction):
    '''
    The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.
    '''
    class_: Literal['https://schema.org/ArriveAction'] = Field( # type: ignore
        default='https://schema.org/ArriveAction',
        alias='@type',
        serialization_alias='@type'
    )
