from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class BusinessEvent(Event):
    """
Event type: Business event.
    """
    type_: Literal['https://schema.org/BusinessEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BusinessEvent'),serialization_alias='class') # type: ignore
