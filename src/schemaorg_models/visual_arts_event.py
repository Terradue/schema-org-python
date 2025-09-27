from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class VisualArtsEvent(Event):
    """
Event type: Visual arts event.
    """
    class_: Literal['https://schema.org/VisualArtsEvent'] = Field(default='https://schema.org/VisualArtsEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
