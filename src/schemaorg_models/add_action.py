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

class AddAction(UpdateAction):
    '''
    The act of editing by adding an object to a collection.
    '''
    class_: Literal['https://schema.org/AddAction'] = Field( # type: ignore
        default='https://schema.org/AddAction',
        alias='@type',
        serialization_alias='@type'
    )
