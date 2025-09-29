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

class WatchAction(ConsumeAction):
    '''
    The act of consuming dynamic/moving visual content.
    '''
    class_: Literal['https://schema.org/WatchAction'] = Field( # type: ignore
        default='https://schema.org/WatchAction',
        alias='@type',
        serialization_alias='@type'
    )
