from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.event import Event

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SaleEvent(Event):
    """
Event type: Sales event.
    """
    class_: Literal['https://schema.org/SaleEvent'] = Field( # type: ignore
        default='https://schema.org/SaleEvent',
        alias='@type',
        serialization_alias='@type'
    )
