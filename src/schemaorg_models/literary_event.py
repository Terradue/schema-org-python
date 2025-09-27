from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class LiteraryEvent(Event):
    """
Event type: Literary event.
    """
    type_: Literal['https://schema.org/LiteraryEvent'] = Field(default='https://schema.org/LiteraryEvent', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
