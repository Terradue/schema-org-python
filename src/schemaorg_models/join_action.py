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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .event import Event

class JoinAction(InteractAction):
    '''
    An agent joins an event/group with participants/friends at a location.\
\
Related actions:\
\
* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.\
* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.\
* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.

    Attributes:
        event: Upcoming or past event associated with this place, organization, or action.
    '''
    class_: Literal['https://schema.org/JoinAction'] = Field( # type: ignore
        default='https://schema.org/JoinAction',
        alias='@type',
        serialization_alias='@type'
    )
    event: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
