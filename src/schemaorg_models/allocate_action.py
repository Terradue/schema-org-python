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
from .organize_action import OrganizeAction

class AllocateAction(OrganizeAction):
    '''
    The act of organizing tasks/objects/events by associating resources to it.
    '''
    class_: Literal['https://schema.org/AllocateAction'] = Field( # type: ignore
        default='https://schema.org/AllocateAction',
        alias='@type',
        serialization_alias='@type'
    )
