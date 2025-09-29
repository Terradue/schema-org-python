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

class CheckAction(FindAction):
    '''
    An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.
    '''
    class_: Literal['https://schema.org/CheckAction'] = Field( # type: ignore
        default='https://schema.org/CheckAction',
        alias='@type',
        serialization_alias='@type'
    )
