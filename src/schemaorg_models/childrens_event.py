from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ChildrensEvent(Event):
    """
Event type: Children's event.
    """
    type_: Literal['https://schema.org/ChildrensEvent'] = Field(default='https://schema.org/ChildrensEvent', alias='@type', serialization_alias='@type') # type: ignore
