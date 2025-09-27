from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.dataset import Dataset

from schemaorg_models.data_feed_item import DataFeedItem
from schemaorg_models.thing import Thing

class DataFeed(Dataset):
    """
A single feed providing structured information about one or more entities or topics.
    """
    class_: Literal['https://schema.org/DataFeed'] = Field(default='https://schema.org/DataFeed', alias='class', serialization_alias='class') # type: ignore
    dataFeedElement: Optional[Union[DataFeedItem, List[DataFeedItem], str, List[str], Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('dataFeedElement', 'https://schema.org/dataFeedElement'), serialization_alias='https://schema.org/dataFeedElement')
