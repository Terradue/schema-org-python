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
    from .organization import Organization
    from .person import Person

class FollowAction(InteractAction):
    '''
    The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.\
\
Related actions:\
\
* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.\
* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.\
* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.\
* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.\
* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it).

    Attributes:
        followee: A sub property of object. The person or organization being followed.
    '''
    class_: Literal['https://schema.org/FollowAction'] = Field( # type: ignore
        default='https://schema.org/FollowAction',
        alias='@type',
        serialization_alias='@type'
    )
    followee: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
