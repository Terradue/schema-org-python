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
from .allocate_action import AllocateAction

class AssignAction(AllocateAction):
    '''
    The act of allocating an action/event/task to some destination (someone or something).
    '''
    class_: Literal['https://schema.org/AssignAction'] = Field( # type: ignore
        default='https://schema.org/AssignAction',
        alias='@type',
        serialization_alias='@type'
    )
