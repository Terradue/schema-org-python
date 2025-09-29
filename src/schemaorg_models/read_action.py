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

class ReadAction(ConsumeAction):
    '''
    The act of consuming written content.
    '''
    class_: Literal['https://schema.org/ReadAction'] = Field( # type: ignore
        default='https://schema.org/ReadAction',
        alias='@type',
        serialization_alias='@type'
    )
