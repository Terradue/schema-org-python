from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ComedyEvent(Event):
    """
Event type: Comedy event.
    """
    class_: Literal['https://schema.org/ComedyEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
