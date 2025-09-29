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
from .creative_work import CreativeWork

class Conversation(CreativeWork):
    '''
    One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.
    '''
    class_: Literal['https://schema.org/Conversation'] = Field( # type: ignore
        default='https://schema.org/Conversation',
        alias='@type',
        serialization_alias='@type'
    )
