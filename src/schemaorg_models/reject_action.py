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

class RejectAction(AllocateAction):
    '''
    The act of rejecting to/adopting an object.\
\
Related actions:\
\
* [[AcceptAction]]: The antonym of RejectAction.
    '''
    class_: Literal['https://schema.org/RejectAction'] = Field( # type: ignore
        default='https://schema.org/RejectAction',
        alias='@type',
        serialization_alias='@type'
    )
