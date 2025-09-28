from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .interact_action import InteractAction

class SubscribeAction(InteractAction):
    """
The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.\
\
Related actions:\
\
* [[FollowAction]]: Unlike FollowAction, SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively pushed for updates.\
* [[RegisterAction]]: Unlike RegisterAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.\
* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.
    """
    class_: Literal['https://schema.org/SubscribeAction'] = Field( # type: ignore
        default='https://schema.org/SubscribeAction',
        alias='@type',
        serialization_alias='@type'
    )
