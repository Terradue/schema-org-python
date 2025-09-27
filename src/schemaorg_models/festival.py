from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class Festival(Event):
    """
Event type: Festival.
    """
    class_: Literal['https://schema.org/Festival'] = Field(default='https://schema.org/Festival', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
