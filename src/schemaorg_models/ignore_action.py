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

class IgnoreAction(AssessAction):
    '''
    The act of intentionally disregarding the object. An agent ignores an object.
    '''
    class_: Literal['https://schema.org/IgnoreAction'] = Field( # type: ignore
        default='https://schema.org/IgnoreAction',
        alias='@type',
        serialization_alias='@type'
    )
