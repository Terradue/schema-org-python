from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class SaleEvent(Event):
    """
Event type: Sales event.
    """
    type_: Literal['https://schema.org/SaleEvent'] = Field(default='https://schema.org/SaleEvent', alias='@type', serialization_alias='@type') # type: ignore
