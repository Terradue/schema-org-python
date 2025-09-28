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

class Hackathon(Event):
    """
A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    """
    class_: Literal['https://schema.org/Hackathon'] = Field( # type: ignore
        default='https://schema.org/Hackathon',
        alias='@type',
        serialization_alias='@type'
    )
