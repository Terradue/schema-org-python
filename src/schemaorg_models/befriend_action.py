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

class BefriendAction(InteractAction):
    '''
    The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.\
\
Related actions:\
\
* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.
    '''
    class_: Literal['https://schema.org/BefriendAction'] = Field( # type: ignore
        default='https://schema.org/BefriendAction',
        alias='@type',
        serialization_alias='@type'
    )
