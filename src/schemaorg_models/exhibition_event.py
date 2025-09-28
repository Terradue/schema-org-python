from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    class_: Literal['https://schema.org/ExhibitionEvent'] = Field( # type: ignore
        default='https://schema.org/ExhibitionEvent',
        alias='@type',
        serialization_alias='@type'
    )
