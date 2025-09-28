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

class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    class_: Literal['https://schema.org/ExhibitionEvent'] = Field( # type: ignore
        default='https://schema.org/ExhibitionEvent',
        alias='@type',
        serialization_alias='@type'
    )
