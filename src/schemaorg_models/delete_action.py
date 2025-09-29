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
from .update_action import UpdateAction

class DeleteAction(UpdateAction):
    '''
    The act of editing a recipient by removing one of its objects.
    '''
    class_: Literal['https://schema.org/DeleteAction'] = Field( # type: ignore
        default='https://schema.org/DeleteAction',
        alias='@type',
        serialization_alias='@type'
    )
