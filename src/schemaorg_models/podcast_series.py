from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .creative_work_series import CreativeWorkSeries
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .performing_group import PerformingGroup
    from .data_feed import DataFeed
    from .person import Person

class PodcastSeries(CreativeWorkSeries):
    """
A podcast is an episodic series of digital audio or video files which a user can download and listen to.
    """
    class_: Literal['https://schema.org/PodcastSeries'] = Field( # type: ignore
        default='https://schema.org/PodcastSeries',
        alias='@type',
        serialization_alias='@type'
    )
    webFeed: Optional[Union["DataFeed", List["DataFeed"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'webFeed',
            'https://schema.org/webFeed'
        ),
        serialization_alias='https://schema.org/webFeed'
    )
    actor: Optional[Union["Person", List["Person"], "PerformingGroup", List["PerformingGroup"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
