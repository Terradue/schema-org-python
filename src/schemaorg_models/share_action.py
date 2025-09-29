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
from .communicate_action import CommunicateAction

class ShareAction(CommunicateAction):
    '''
    The act of distributing content to people for their amusement or edification.
    '''
    class_: Literal['https://schema.org/ShareAction'] = Field( # type: ignore
        default='https://schema.org/ShareAction',
        alias='@type',
        serialization_alias='@type'
    )
