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
from .assess_action import AssessAction

class ReactAction(AssessAction):
    '''
    The act of responding instinctively and emotionally to an object, expressing a sentiment.
    '''
    class_: Literal['https://schema.org/ReactAction'] = Field( # type: ignore
        default='https://schema.org/ReactAction',
        alias='@type',
        serialization_alias='@type'
    )
