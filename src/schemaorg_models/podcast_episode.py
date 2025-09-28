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

class PodcastEpisode(Episode):
    """
A single episode of a podcast series.
    """
    class_: Literal['https://schema.org/PodcastEpisode'] = Field( # type: ignore
        default='https://schema.org/PodcastEpisode',
        alias='@type',
        serialization_alias='@type'
    )
