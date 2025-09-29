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
from .interact_action import InteractAction

class MarryAction(InteractAction):
    '''
    The act of marrying a person.
    '''
    class_: Literal['https://schema.org/MarryAction'] = Field( # type: ignore
        default='https://schema.org/MarryAction',
        alias='@type',
        serialization_alias='@type'
    )
