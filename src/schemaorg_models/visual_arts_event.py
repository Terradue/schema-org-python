from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class VisualArtsEvent(Event):
    """
Event type: Visual arts event.
    """
    type_: Literal['https://schema.org/VisualArtsEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VisualArtsEvent'),serialization_alias='class') # type: ignore
