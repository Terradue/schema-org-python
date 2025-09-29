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

class PrependAction(InsertAction):
    '''
    The act of inserting at the beginning if an ordered collection.
    '''
    class_: Literal['https://schema.org/PrependAction'] = Field( # type: ignore
        default='https://schema.org/PrependAction',
        alias='@type',
        serialization_alias='@type'
    )
