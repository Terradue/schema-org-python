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
from .message import Message

class EmailMessage(Message):
    '''
    An email message.
    '''
    class_: Literal['https://schema.org/EmailMessage'] = Field( # type: ignore
        default='https://schema.org/EmailMessage',
        alias='@type',
        serialization_alias='@type'
    )
