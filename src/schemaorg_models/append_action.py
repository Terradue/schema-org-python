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
from .insert_action import InsertAction

class AppendAction(InsertAction):
    '''
    The act of inserting at the end if an ordered collection.
    '''
    class_: Literal['https://schema.org/AppendAction'] = Field( # type: ignore
        default='https://schema.org/AppendAction',
        alias='@type',
        serialization_alias='@type'
    )
