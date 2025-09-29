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
from .create_action import CreateAction

class DrawAction(CreateAction):
    '''
    The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    '''
    class_: Literal['https://schema.org/DrawAction'] = Field( # type: ignore
        default='https://schema.org/DrawAction',
        alias='@type',
        serialization_alias='@type'
    )
