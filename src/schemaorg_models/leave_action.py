from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.interact_action import InteractAction

from schemaorg_models.event import Event

class LeaveAction(InteractAction):
    """
An agent leaves an event / group with participants/friends at a location.\
\
Related actions:\
\
* [[JoinAction]]: The antonym of LeaveAction.\
* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.
    """
    type_: Literal['https://schema.org/LeaveAction'] = Field(default='https://schema.org/LeaveAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    event: Optional[Union[Event, List[Event]]] = Field(default=None, validation_alias=AliasChoices('event', 'https://schema.org/event'), serialization_alias='https://schema.org/event')
