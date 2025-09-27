from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class SaleEvent(Event):
    """
Event type: Sales event.
    """
    class_: Literal['https://schema.org/SaleEvent'] = Field(default='https://schema.org/SaleEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
