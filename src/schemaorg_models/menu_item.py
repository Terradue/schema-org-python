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
    from .demand import Demand
    from .restricted_diet import RestrictedDiet
    from .menu_section import MenuSection
    from .offer import Offer
    from .nutrition_information import NutritionInformation

class MenuItem(Intangible):
    '''
    A food or drink item listed in a menu or menu section.

    Attributes:
        suitableForDiet: Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc.
        menuAddOn: Additional menu item(s) such as a side dish of salad or side order of fries that can be added to this menu item. Additionally it can be a menu section containing allowed add-on menu items for this menu item.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
        nutrition: Nutrition information about the recipe or menu item.
    '''
    class_: Literal['https://schema.org/MenuItem'] = Field( # type: ignore
        default='https://schema.org/MenuItem',
        alias='@type',
        serialization_alias='@type'
    )
    suitableForDiet: Optional[Union['RestrictedDiet', List['RestrictedDiet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    menuAddOn: Optional[Union['MenuItem', List['MenuItem'], 'MenuSection', List['MenuSection']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    nutrition: Optional[Union['NutritionInformation', List['NutritionInformation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
