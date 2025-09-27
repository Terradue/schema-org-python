from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work_season import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    """
A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.
    """
    type_: Literal['https://schema.org/PodcastSeason'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PodcastSeason'),serialization_alias='class') # type: ignore
