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
from .use_action import UseAction

class WearAction(UseAction):
    '''
    The act of dressing oneself in clothing.
    '''
    class_: Literal['https://schema.org/WearAction'] = Field( # type: ignore
        default='https://schema.org/WearAction',
        alias='@type',
        serialization_alias='@type'
    )
