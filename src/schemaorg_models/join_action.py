from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.interact_action import InteractAction

from schemaorg_models.event import Event

class JoinAction(InteractAction):
    """
An agent joins an event/group with participants/friends at a location.\
\
Related actions:\
\
* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.\
* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.\
* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.
    """
    event: Optional[Union[Event, List[Event]]] = Field(default=None,validation_alias=AliasChoices('event', 'https://schema.org/event'),serialization_alias='https://schema.org/event')
