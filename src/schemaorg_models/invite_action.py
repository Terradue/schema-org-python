from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.event import Event

class InviteAction(CommunicateAction):
    """
The act of asking someone to attend an event. Reciprocal of RsvpAction.
    """
    type_: Literal['https://schema.org/InviteAction'] = Field(default='https://schema.org/InviteAction', alias='@type', serialization_alias='@type') # type: ignore
    event: Optional[Union[Event, List[Event]]] = Field(default=None, validation_alias=AliasChoices('event', 'https://schema.org/event'), serialization_alias='https://schema.org/event')
