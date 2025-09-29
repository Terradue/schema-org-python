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
from .achieve_action import AchieveAction

class TieAction(AchieveAction):
    '''
    The act of reaching a draw in a competitive activity.
    '''
    class_: Literal['https://schema.org/TieAction'] = Field( # type: ignore
        default='https://schema.org/TieAction',
        alias='@type',
        serialization_alias='@type'
    )
