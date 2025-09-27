from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class ComedyEvent(Event):
    """
Event type: Comedy event.
    """
    type_: Literal['https://schema.org/ComedyEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ComedyEvent'),serialization_alias='class') # type: ignore
