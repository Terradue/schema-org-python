from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.event import Event

class InviteAction(CommunicateAction):
    """
The act of asking someone to attend an event. Reciprocal of RsvpAction.
    """
    event: Optional[Union[Event, List[Event]]] = Field(default=None,validation_alias=AliasChoices('event', 'https://schema.org/event'),serialization_alias='https://schema.org/event')
