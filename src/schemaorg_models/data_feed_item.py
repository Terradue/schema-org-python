from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.thing import Thing

class DataFeedItem(Intangible):
    """
A single item within a larger data feed.
    """
    class_: Literal['https://schema.org/DataFeedItem'] = Field(default='https://schema.org/DataFeedItem', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    item: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('item', 'https://schema.org/item'), serialization_alias='https://schema.org/item')
    dateCreated: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('dateCreated', 'https://schema.org/dateCreated'), serialization_alias='https://schema.org/dateCreated')
    dateDeleted: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None, validation_alias=AliasChoices('dateDeleted', 'https://schema.org/dateDeleted'), serialization_alias='https://schema.org/dateDeleted')
    dateModified: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None, validation_alias=AliasChoices('dateModified', 'https://schema.org/dateModified'), serialization_alias='https://schema.org/dateModified')
