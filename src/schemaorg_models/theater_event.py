from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class TheaterEvent(Event):
    """
Event type: Theater performance.
    """
    type_: Literal['https://schema.org/TheaterEvent'] = Field(default='https://schema.org/TheaterEvent', alias='@type', serialization_alias='@type') # type: ignore
