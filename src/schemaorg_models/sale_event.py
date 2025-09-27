from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class SaleEvent(Event):
    """
Event type: Sales event.
    """
    type_: Literal['https://schema.org/SaleEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SaleEvent'),serialization_alias='class') # type: ignore
