from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class BusinessEvent(Event):
    """
Event type: Business event.
    """
    class_: Literal['https://schema.org/BusinessEvent'] = Field(default='https://schema.org/BusinessEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
