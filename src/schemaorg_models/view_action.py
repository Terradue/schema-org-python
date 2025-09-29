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

class ViewAction(ConsumeAction):
    '''
    The act of consuming static visual content.
    '''
    class_: Literal['https://schema.org/ViewAction'] = Field( # type: ignore
        default='https://schema.org/ViewAction',
        alias='@type',
        serialization_alias='@type'
    )
