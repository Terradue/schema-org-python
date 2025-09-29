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

class InstallAction(ConsumeAction):
    '''
    The act of installing an application.
    '''
    class_: Literal['https://schema.org/InstallAction'] = Field( # type: ignore
        default='https://schema.org/InstallAction',
        alias='@type',
        serialization_alias='@type'
    )
