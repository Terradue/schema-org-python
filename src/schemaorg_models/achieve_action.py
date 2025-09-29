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
from .action import Action

class AchieveAction(Action):
    '''
    The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.
    '''
    class_: Literal['https://schema.org/AchieveAction'] = Field( # type: ignore
        default='https://schema.org/AchieveAction',
        alias='@type',
        serialization_alias='@type'
    )
