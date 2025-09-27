from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class DanceEvent(Event):
    """
Event type: A social dance.
    """
    class_: Literal['https://schema.org/DanceEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
