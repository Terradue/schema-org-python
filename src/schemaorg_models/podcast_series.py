from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work_series import CreativeWorkSeries

from schemaorg_models.data_feed import DataFeed
from schemaorg_models.person import Person
from schemaorg_models.performing_group import PerformingGroup

class PodcastSeries(CreativeWorkSeries):
    """
A podcast is an episodic series of digital audio or video files which a user can download and listen to.
    """
    webFeed: Optional[Union[DataFeed, List[DataFeed], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('webFeed', 'https://schema.org/webFeed'),serialization_alias='https://schema.org/webFeed')
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(default=None,validation_alias=AliasChoices('actor', 'https://schema.org/actor'),serialization_alias='https://schema.org/actor')
