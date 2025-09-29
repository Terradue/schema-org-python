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
from .consume_action import ConsumeAction

class UseAction(ConsumeAction):
    '''
    The act of applying an object to its intended purpose.
    '''
    class_: Literal['https://schema.org/UseAction'] = Field( # type: ignore
        default='https://schema.org/UseAction',
        alias='@type',
        serialization_alias='@type'
    )
