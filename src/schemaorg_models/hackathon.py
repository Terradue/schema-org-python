from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class Hackathon(Event):
    """
A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    """
    class_: Literal['https://schema.org/Hackathon'] = Field(default='https://schema.org/Hackathon', alias='@type', serialization_alias='@type') # type: ignore
