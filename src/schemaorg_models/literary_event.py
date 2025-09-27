from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class LiteraryEvent(Event):
    """
Event type: Literary event.
    """
    type_: Literal['https://schema.org/LiteraryEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LiteraryEvent'),serialization_alias='class') # type: ignore
