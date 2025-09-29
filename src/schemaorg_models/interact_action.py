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

class InteractAction(Action):
    '''
    The act of interacting with another person or organization.
    '''
    class_: Literal['https://schema.org/InteractAction'] = Field( # type: ignore
        default='https://schema.org/InteractAction',
        alias='@type',
        serialization_alias='@type'
    )
