from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class Hackathon(Event):
    """
A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    """
    type_: Literal['https://schema.org/Hackathon'] = Field(default='https://schema.org/Hackathon', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
