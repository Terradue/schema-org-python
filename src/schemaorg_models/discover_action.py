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
from .find_action import FindAction

class DiscoverAction(FindAction):
    '''
    The act of discovering/finding an object.
    '''
    class_: Literal['https://schema.org/DiscoverAction'] = Field( # type: ignore
        default='https://schema.org/DiscoverAction',
        alias='@type',
        serialization_alias='@type'
    )
