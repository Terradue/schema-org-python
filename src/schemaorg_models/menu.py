from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.menu_item import MenuItem

class Menu(CreativeWork):
    """
A structured representation of food or drink items available from a FoodEstablishment.
    """
    class_: Literal['https://schema.org/Menu'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    hasMenuItem: Optional[Union[MenuItem, List[MenuItem]]] = Field(default=None,validation_alias=AliasChoices('hasMenuItem', 'https://schema.org/hasMenuItem'), serialization_alias='https://schema.org/hasMenuItem')
    hasMenuSection: Optional[Union["MenuSection", List["MenuSection"]]] = Field(default=None,validation_alias=AliasChoices('hasMenuSection', 'https://schema.org/hasMenuSection'), serialization_alias='https://schema.org/hasMenuSection')
