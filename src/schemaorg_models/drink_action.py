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

class DrinkAction(ConsumeAction):
    '''
    The act of swallowing liquids.
    '''
    class_: Literal['https://schema.org/DrinkAction'] = Field( # type: ignore
        default='https://schema.org/DrinkAction',
        alias='@type',
        serialization_alias='@type'
    )
