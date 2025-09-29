from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    AliasChoices,
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
    from .offer import Offer
    from .physical_activity_category import PhysicalActivityCategory
    from .category_code import CategoryCode
    from .geo_shape import GeoShape
    from .media_subscription import MediaSubscription
    from .thing import Thing
    from .place import Place

class ActionAccessSpecification(Intangible):
    """
A set of requirements that must be fulfilled in order to perform an Action.
    """
    class_: Literal['https://schema.org/ActionAccessSpecification'] = Field( # type: ignore
        default='https://schema.org/ActionAccessSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    requiresSubscription: Optional[Union[bool, List[bool], "MediaSubscription", List["MediaSubscription"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiresSubscription',
            'https://schema.org/requiresSubscription'
        ),
        serialization_alias='https://schema.org/requiresSubscription'
    )
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectsAcceptanceOf',
            'https://schema.org/expectsAcceptanceOf'
        ),
        serialization_alias='https://schema.org/expectsAcceptanceOf'
    )
    eligibleRegion: Optional[Union["GeoShape", List["GeoShape"], str, List[str], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion',
            'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion'
    )
    availabilityEnds: Optional[Union[date, List[date], time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityEnds',
            'https://schema.org/availabilityEnds'
        ),
        serialization_alias='https://schema.org/availabilityEnds'
    )
    ineligibleRegion: Optional[Union[str, List[str], "Place", List["Place"], "GeoShape", List["GeoShape"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion',
            'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion'
    )
    availabilityStarts: Optional[Union[datetime, List[datetime], date, List[date], time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityStarts',
            'https://schema.org/availabilityStarts'
        ),
        serialization_alias='https://schema.org/availabilityStarts'
    )
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], "Thing", List["Thing"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
