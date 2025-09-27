from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class TheaterEvent(Event):
    """
Event type: Theater performance.
    """
    class_: Literal['https://schema.org/TheaterEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
