from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .interact_action import InteractAction

class RegisterAction(InteractAction):
    """
The act of registering to be a user of a service, product or web page.\
\
Related actions:\
\
* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.\
* [[FollowAction]]: Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.\
* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object.
    """
    class_: Literal['https://schema.org/RegisterAction'] = Field( # type: ignore
        default='https://schema.org/RegisterAction',
        alias='@type',
        serialization_alias='@type'
    )
