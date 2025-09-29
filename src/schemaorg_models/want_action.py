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

class WantAction(ReactAction):
    '''
    The act of expressing a desire about the object. An agent wants an object.
    '''
    class_: Literal['https://schema.org/WantAction'] = Field( # type: ignore
        default='https://schema.org/WantAction',
        alias='@type',
        serialization_alias='@type'
    )
