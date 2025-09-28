from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    class_: Literal['https://schema.org/ExhibitionEvent'] = Field( # type: ignore
        default='https://schema.org/ExhibitionEvent',
        alias='@type',
        serialization_alias='@type'
    )
