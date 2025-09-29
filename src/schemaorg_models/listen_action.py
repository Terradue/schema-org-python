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

class ListenAction(ConsumeAction):
    '''
    The act of consuming audio content.
    '''
    class_: Literal['https://schema.org/ListenAction'] = Field( # type: ignore
        default='https://schema.org/ListenAction',
        alias='@type',
        serialization_alias='@type'
    )
