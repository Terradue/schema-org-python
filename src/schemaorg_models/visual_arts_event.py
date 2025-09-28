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

class VisualArtsEvent(Event):
    """
Event type: Visual arts event.
    """
    class_: Literal['https://schema.org/VisualArtsEvent'] = Field( # type: ignore
        default='https://schema.org/VisualArtsEvent',
        alias='@type',
        serialization_alias='@type'
    )
