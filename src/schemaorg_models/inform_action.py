from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.event import Event

class InformAction(CommunicateAction):
    """
The act of notifying someone of information pertinent to them, with no expectation of a response.
    """
    class_: Literal['https://schema.org/InformAction'] = Field(default='https://schema.org/InformAction', alias='@type', serialization_alias='@type') # type: ignore
    event: Optional[Union[Event, List[Event]]] = Field(default=None, validation_alias=AliasChoices('event', 'https://schema.org/event'), serialization_alias='https://schema.org/event')
