from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class BusinessEvent(Event):
    """
Event type: Business event.
    """
    class_: Literal['https://schema.org/BusinessEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
