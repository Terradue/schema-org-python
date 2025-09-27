from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work_series import CreativeWorkSeries

from schemaorg_models.data_feed import DataFeed
from schemaorg_models.person import Person
from schemaorg_models.performing_group import PerformingGroup

class PodcastSeries(CreativeWorkSeries):
    """
A podcast is an episodic series of digital audio or video files which a user can download and listen to.
    """
    type_: Literal['https://schema.org/PodcastSeries'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PodcastSeries'),serialization_alias='class') # type: ignore
    webFeed: Optional[Union[DataFeed, List[DataFeed], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('webFeed', 'https://schema.org/webFeed'),serialization_alias='https://schema.org/webFeed')
    @field_serializer('webFeed')
    def webFeed2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(default=None,validation_alias=AliasChoices('actor', 'https://schema.org/actor'),serialization_alias='https://schema.org/actor')
