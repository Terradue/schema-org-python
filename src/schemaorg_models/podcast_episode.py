from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.episode import Episode


class PodcastEpisode(Episode):
    """
A single episode of a podcast series.
    """
    type_: Literal['https://schema.org/PodcastEpisode'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PodcastEpisode'),serialization_alias='class') # type: ignore
