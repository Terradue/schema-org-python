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
from .status_enumeration import StatusEnumeration

class ActionStatusType(StatusEnumeration):
    '''
    The status of an Action.
    '''
    class_: Literal['https://schema.org/ActionStatusType'] = Field( # type: ignore
        default='https://schema.org/ActionStatusType',
        alias='@type',
        serialization_alias='@type'
    )
