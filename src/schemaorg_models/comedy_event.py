from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ComedyEvent(Event):
    """
Event type: Comedy event.
    """
    type_: Literal['https://schema.org/ComedyEvent'] = Field(default='https://schema.org/ComedyEvent', alias='@type', serialization_alias='@type') # type: ignore
