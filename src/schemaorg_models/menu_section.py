from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.menu_item import MenuItem

class MenuSection(CreativeWork):
    """
A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast', etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other classification made by the menu provider.
    """
    class_: Literal['https://schema.org/MenuSection'] = Field( # type: ignore
        default='https://schema.org/MenuSection',
        alias='@type',
        serialization_alias='@type'
    )
    hasMenuItem: Optional[Union[MenuItem, List[MenuItem]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenuItem',
            'https://schema.org/hasMenuItem'
        ),
        serialization_alias='https://schema.org/hasMenuItem'
    )
    hasMenuSection: Optional[Union["MenuSection", List["MenuSection"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenuSection',
            'https://schema.org/hasMenuSection'
        ),
        serialization_alias='https://schema.org/hasMenuSection'
    )
