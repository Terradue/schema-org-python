from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .thing import Thing

class DataFeedItem(Intangible):
    '''
    A single item within a larger data feed.

    Attributes:
        item: An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
        dateCreated: The date on which the CreativeWork was created or the item was added to a DataFeed.
        dateDeleted: The datetime the item was removed from the DataFeed.
        dateModified: The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
    '''
    class_: Literal['https://schema.org/DataFeedItem'] = Field( # type: ignore
        default='https://schema.org/DataFeedItem',
        alias='@type',
        serialization_alias='@type'
    )
    item: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dateCreated: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dateDeleted: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dateModified: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
