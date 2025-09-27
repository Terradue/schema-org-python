from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class ChildrensEvent(Event):
    """
Event type: Children's event.
    """
    type_: Literal['https://schema.org/ChildrensEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ChildrensEvent'),serialization_alias='class') # type: ignore
