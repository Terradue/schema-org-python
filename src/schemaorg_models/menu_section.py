from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.menu_item import MenuItem

class MenuSection(CreativeWork):
    """
A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast', etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other classification made by the menu provider.
    """
    class_: Literal['https://schema.org/MenuSection'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    hasMenuItem: Optional[Union[MenuItem, List[MenuItem]]] = Field(default=None,validation_alias=AliasChoices('hasMenuItem', 'https://schema.org/hasMenuItem'), serialization_alias='https://schema.org/hasMenuItem')
    hasMenuSection: Optional[Union["MenuSection", List["MenuSection"]]] = Field(default=None,validation_alias=AliasChoices('hasMenuSection', 'https://schema.org/hasMenuSection'), serialization_alias='https://schema.org/hasMenuSection')
