from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ComedyEvent(Event):
    """
Event type: Comedy event.
    """
    class_: Literal['https://schema.org/ComedyEvent'] = Field(default='https://schema.org/ComedyEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
