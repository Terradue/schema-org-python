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
from .react_action import ReactAction

class LikeAction(ReactAction):
    '''
    The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    '''
    class_: Literal['https://schema.org/LikeAction'] = Field( # type: ignore
        default='https://schema.org/LikeAction',
        alias='@type',
        serialization_alias='@type'
    )
