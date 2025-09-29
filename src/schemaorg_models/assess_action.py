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
from .action import Action

class AssessAction(Action):
    '''
    The act of forming one's opinion, reaction or sentiment.
    '''
    class_: Literal['https://schema.org/AssessAction'] = Field( # type: ignore
        default='https://schema.org/AssessAction',
        alias='@type',
        serialization_alias='@type'
    )
