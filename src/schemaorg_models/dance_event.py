from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class DanceEvent(Event):
    """
Event type: A social dance.
    """
    type_: Literal['https://schema.org/DanceEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DanceEvent'),serialization_alias='class') # type: ignore
