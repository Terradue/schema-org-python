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
from .interact_action import InteractAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .organization import Organization

class FollowAction(InteractAction):
    """
The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.\
\
Related actions:\
\
* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.\
* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.\
* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.\
* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.\
* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it).
    """
    class_: Literal['https://schema.org/FollowAction'] = Field( # type: ignore
        default='https://schema.org/FollowAction',
        alias='@type',
        serialization_alias='@type'
    )
    followee: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'followee',
            'https://schema.org/followee'
        ),
        serialization_alias='https://schema.org/followee'
    )
