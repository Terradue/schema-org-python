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
    from .item_list_order_type import ItemListOrderType
    from .list_item import ListItem
    from .thing import Thing

class ItemList(Intangible):
    '''
    A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.

    Attributes:
        numberOfItems: The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.
        aggregateElement: Indicates a prototype of the elements in the list that is used to hold aggregate information (ratings, offers, etc.).
        itemListOrder: Type of ordering (e.g. Ascending, Descending, Unordered).
        itemListElement: For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.\
\
Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.\
\
Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.
    '''
    class_: Literal['https://schema.org/ItemList'] = Field( # type: ignore
        default='https://schema.org/ItemList',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfItems: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfItems',
            'https://schema.org/numberOfItems'
        ),
        serialization_alias='https://schema.org/numberOfItems'
    )
    aggregateElement: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateElement',
            'https://schema.org/aggregateElement'
        ),
        serialization_alias='https://schema.org/aggregateElement'
    )
    itemListOrder: Optional[Union['ItemListOrderType', List['ItemListOrderType'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemListOrder',
            'https://schema.org/itemListOrder'
        ),
        serialization_alias='https://schema.org/itemListOrder'
    )
    itemListElement: Optional[Union[str, List[str], 'Thing', List['Thing'], 'ListItem', List['ListItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemListElement',
            'https://schema.org/itemListElement'
        ),
        serialization_alias='https://schema.org/itemListElement'
    )
