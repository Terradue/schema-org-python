from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class BusinessEvent(Event):
    """
Event type: Business event.
    """
    class_: Literal['https://schema.org/BusinessEvent'] = Field(default='https://schema.org/BusinessEvent', alias='@type', serialization_alias='@type') # type: ignore
