from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class DanceEvent(Event):
    """
Event type: A social dance.
    """
    type_: Literal['https://schema.org/DanceEvent'] = Field(default='https://schema.org/DanceEvent', alias='@type', serialization_alias='@type') # type: ignore
