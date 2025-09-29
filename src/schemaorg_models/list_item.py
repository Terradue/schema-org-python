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

class ListItem(Intangible):
    '''
    An list item, e.g. a step in a checklist or how-to description.

    Attributes:
        position: The position of an item in a series or sequence of items.
        nextItem: A link to the ListItem that follows the current one.
        item: An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
        previousItem: A link to the ListItem that precedes the current one.
    '''
    class_: Literal['https://schema.org/ListItem'] = Field( # type: ignore
        default='https://schema.org/ListItem',
        alias='@type',
        serialization_alias='@type'
    )
    position: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    nextItem: Optional[Union['ListItem', List['ListItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    item: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    previousItem: Optional[Union['ListItem', List['ListItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
