from __future__ import annotations
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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .demand import Demand
    from .restricted_diet import RestrictedDiet
    from .menu_section import MenuSection
    from .nutrition_information import NutritionInformation
    from .offer import Offer

class MenuItem(Intangible):
    """
A food or drink item listed in a menu or menu section.
    """
    class_: Literal['https://schema.org/MenuItem'] = Field( # type: ignore
        default='https://schema.org/MenuItem',
        alias='@type',
        serialization_alias='@type'
    )
    suitableForDiet: Optional[Union["RestrictedDiet", List["RestrictedDiet"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suitableForDiet',
            'https://schema.org/suitableForDiet'
        ),
        serialization_alias='https://schema.org/suitableForDiet'
    )
    menuAddOn: Optional[Union["MenuItem", List["MenuItem"], "MenuSection", List["MenuSection"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'menuAddOn',
            'https://schema.org/menuAddOn'
        ),
        serialization_alias='https://schema.org/menuAddOn'
    )
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    nutrition: Optional[Union["NutritionInformation", List["NutritionInformation"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nutrition',
            'https://schema.org/nutrition'
        ),
        serialization_alias='https://schema.org/nutrition'
    )
