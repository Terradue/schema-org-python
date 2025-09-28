from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .event import Event
from .interact_action import InteractAction

class LeaveAction(InteractAction):
    """
An agent leaves an event / group with participants/friends at a location.\
\
Related actions:\
\
* [[JoinAction]]: The antonym of LeaveAction.\
* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.
    """
    class_: Literal['https://schema.org/LeaveAction'] = Field( # type: ignore
        default='https://schema.org/LeaveAction',
        alias='@type',
        serialization_alias='@type'
    )
    event: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
