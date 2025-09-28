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

class Festival(Event):
    """
Event type: Festival.
    """
    class_: Literal['https://schema.org/Festival'] = Field( # type: ignore
        default='https://schema.org/Festival',
        alias='@type',
        serialization_alias='@type'
    )
