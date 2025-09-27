from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class DanceEvent(Event):
    """
Event type: A social dance.
    """
    class_: Literal['https://schema.org/DanceEvent'] = Field(default='https://schema.org/DanceEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
