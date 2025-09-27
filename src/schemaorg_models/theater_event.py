from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class TheaterEvent(Event):
    """
Event type: Theater performance.
    """
    type_: Literal['https://schema.org/TheaterEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TheaterEvent'),serialization_alias='class') # type: ignore
