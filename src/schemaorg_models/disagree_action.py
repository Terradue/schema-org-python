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

class DisagreeAction(ReactAction):
    '''
    The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.
    '''
    class_: Literal['https://schema.org/DisagreeAction'] = Field( # type: ignore
        default='https://schema.org/DisagreeAction',
        alias='@type',
        serialization_alias='@type'
    )
