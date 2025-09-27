from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work_season import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    """
A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.
    """
    class_: Literal['https://schema.org/PodcastSeason'] = Field(default='https://schema.org/PodcastSeason', alias='class', serialization_alias='class') # type: ignore
