from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class Hackathon(Event):
    """
A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    """
    type_: Literal['https://schema.org/Hackathon'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Hackathon'),serialization_alias='class') # type: ignore
