from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    type_: Literal['https://schema.org/ExhibitionEvent'] = Field(default='https://schema.org/ExhibitionEvent', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
