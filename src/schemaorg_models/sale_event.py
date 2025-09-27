from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class SaleEvent(Event):
    """
Event type: Sales event.
    """
    class_: Literal['https://schema.org/SaleEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
