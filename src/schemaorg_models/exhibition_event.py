from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    class_: Literal['https://schema.org/ExhibitionEvent'] = Field(default='https://schema.org/ExhibitionEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
