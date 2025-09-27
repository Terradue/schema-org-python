from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.interact_action import InteractAction


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
    type_: Literal['https://schema.org/SubscribeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SubscribeAction'),serialization_alias='class') # type: ignore
