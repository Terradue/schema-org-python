from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.episode import Episode

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RadioEpisode(Episode):
    """
A radio episode which can be part of a series or season.
    """
    class_: Literal['https://schema.org/RadioEpisode'] = Field( # type: ignore
        default='https://schema.org/RadioEpisode',
        alias='@type',
        serialization_alias='@type'
    )
