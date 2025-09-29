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
from .allocate_action import AllocateAction

class AcceptAction(AllocateAction):
    '''
    The act of committing to/adopting an object.\
\
Related actions:\
\
* [[RejectAction]]: The antonym of AcceptAction.
    '''
    class_: Literal['https://schema.org/AcceptAction'] = Field( # type: ignore
        default='https://schema.org/AcceptAction',
        alias='@type',
        serialization_alias='@type'
    )
