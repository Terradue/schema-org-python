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

class FindAction(Action):
    '''
    The act of finding an object.\
\
Related actions:\
\
* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.
    '''
    class_: Literal['https://schema.org/FindAction'] = Field( # type: ignore
        default='https://schema.org/FindAction',
        alias='@type',
        serialization_alias='@type'
    )
