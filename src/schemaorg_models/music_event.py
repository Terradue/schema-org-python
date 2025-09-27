from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class MusicEvent(Event):
    """
Event type: Music event.
    """
    class_: Literal['https://schema.org/MusicEvent'] = Field(default='https://schema.org/MusicEvent', alias='@type', serialization_alias='@type') # type: ignore
