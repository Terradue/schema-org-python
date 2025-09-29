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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .menu_item import MenuItem

class MenuSection(CreativeWork):
    '''
    A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast', etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other classification made by the menu provider.

    Attributes:
        hasMenuItem: A food or drink item contained in a menu or menu section.
        hasMenuSection: A subgrouping of the menu (by dishes, course, serving time period, etc.).
    '''
    class_: Literal['https://schema.org/MenuSection'] = Field( # type: ignore
        default='https://schema.org/MenuSection',
        alias='@type',
        serialization_alias='@type'
    )
    hasMenuItem: Optional[Union['MenuItem', List['MenuItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasMenuSection: Optional[Union['MenuSection', List['MenuSection']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
