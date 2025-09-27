from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class VisualArtsEvent(Event):
    """
Event type: Visual arts event.
    """
    type_: Literal['https://schema.org/VisualArtsEvent'] = Field(default='https://schema.org/VisualArtsEvent', alias='@type', serialization_alias='@type') # type: ignore
