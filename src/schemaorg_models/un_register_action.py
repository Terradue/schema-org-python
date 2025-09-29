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

class UnRegisterAction(InteractAction):
    '''
    The act of un-registering from a service.\
\
Related actions:\
\
* [[RegisterAction]]: antonym of UnRegisterAction.\
* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.
    '''
    class_: Literal['https://schema.org/UnRegisterAction'] = Field( # type: ignore
        default='https://schema.org/UnRegisterAction',
        alias='@type',
        serialization_alias='@type'
    )
