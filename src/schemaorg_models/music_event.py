from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class MusicEvent(Event):
    """
Event type: Music event.
    """
    type_: Literal['https://schema.org/MusicEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicEvent'),serialization_alias='class') # type: ignore
