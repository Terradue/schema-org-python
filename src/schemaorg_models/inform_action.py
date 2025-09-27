from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.event import Event

class InformAction(CommunicateAction):
    """
The act of notifying someone of information pertinent to them, with no expectation of a response.
    """
    type_: Literal['https://schema.org/InformAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InformAction'),serialization_alias='class') # type: ignore
    event: Optional[Union[Event, List[Event]]] = Field(default=None,validation_alias=AliasChoices('event', 'https://schema.org/event'),serialization_alias='https://schema.org/event')
