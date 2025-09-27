from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.thing import Thing
from schemaorg_models.list_item import ListItem

class ItemList(Intangible):
    """
A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.
    """
    type_: Literal['https://schema.org/ItemList'] = Field(default='https://schema.org/ItemList', alias='@type', serialization_alias='@type') # type: ignore
    numberOfItems: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('numberOfItems', 'https://schema.org/numberOfItems'), serialization_alias='https://schema.org/numberOfItems')
    aggregateElement: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('aggregateElement', 'https://schema.org/aggregateElement'), serialization_alias='https://schema.org/aggregateElement')
    itemListOrder: Optional[Union["ItemListOrderType", List["ItemListOrderType"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('itemListOrder', 'https://schema.org/itemListOrder'), serialization_alias='https://schema.org/itemListOrder')
    itemListElement: Optional[Union[str, List[str], Thing, List[Thing], ListItem, List[ListItem]]] = Field(default=None, validation_alias=AliasChoices('itemListElement', 'https://schema.org/itemListElement'), serialization_alias='https://schema.org/itemListElement')
