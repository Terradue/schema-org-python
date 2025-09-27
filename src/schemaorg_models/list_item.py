from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.thing import Thing

class ListItem(Intangible):
    """
An list item, e.g. a step in a checklist or how-to description.
    """
    class_: Literal['https://schema.org/ListItem'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    position: Optional[Union[int, List[int], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('position', 'https://schema.org/position'), serialization_alias='https://schema.org/position')
    nextItem: Optional[Union["ListItem", List["ListItem"]]] = Field(default=None,validation_alias=AliasChoices('nextItem', 'https://schema.org/nextItem'), serialization_alias='https://schema.org/nextItem')
    item: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('item', 'https://schema.org/item'), serialization_alias='https://schema.org/item')
    previousItem: Optional[Union["ListItem", List["ListItem"]]] = Field(default=None,validation_alias=AliasChoices('previousItem', 'https://schema.org/previousItem'), serialization_alias='https://schema.org/previousItem')
