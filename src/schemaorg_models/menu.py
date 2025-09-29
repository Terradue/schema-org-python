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
    from .menu_section import MenuSection
    from .menu_item import MenuItem

class Menu(CreativeWork):
    '''
    A structured representation of food or drink items available from a FoodEstablishment.

    Attributes:
        hasMenuItem: A food or drink item contained in a menu or menu section.
        hasMenuSection: A subgrouping of the menu (by dishes, course, serving time period, etc.).
    '''
    class_: Literal['https://schema.org/Menu'] = Field( # type: ignore
        default='https://schema.org/Menu',
        alias='@type',
        serialization_alias='@type'
    )
    hasMenuItem: Optional[Union['MenuItem', List['MenuItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenuItem',
            'https://schema.org/hasMenuItem'
        ),
        serialization_alias='https://schema.org/hasMenuItem'
    )
    hasMenuSection: Optional[Union['MenuSection', List['MenuSection']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenuSection',
            'https://schema.org/hasMenuSection'
        ),
        serialization_alias='https://schema.org/hasMenuSection'
    )
