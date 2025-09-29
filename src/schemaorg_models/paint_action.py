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

class PaintAction(CreateAction):
    '''
    The act of producing a painting, typically with paint and canvas as instruments.
    '''
    class_: Literal['https://schema.org/PaintAction'] = Field( # type: ignore
        default='https://schema.org/PaintAction',
        alias='@type',
        serialization_alias='@type'
    )
