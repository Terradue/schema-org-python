from typing import Literal
from pydantic import Field
from schemaorg_models.episode import Episode


class PodcastEpisode(Episode):
    """
A single episode of a podcast series.
    """
    type_: Literal['https://schema.org/PodcastEpisode'] = Field(default='https://schema.org/PodcastEpisode', alias='@type', serialization_alias='@type') # type: ignore
