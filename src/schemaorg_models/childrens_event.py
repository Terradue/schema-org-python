from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ChildrensEvent(Event):
    """
Event type: Children's event.
    """
    type_: Literal['https://schema.org/ChildrensEvent'] = Field(default='https://schema.org/ChildrensEvent', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
