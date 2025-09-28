from __future__ import annotations

from .place import Place    

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

class TouristAttraction(Place):
    """
A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)
    """
    class_: Literal['https://schema.org/TouristAttraction'] = Field( # type: ignore
        default='https://schema.org/TouristAttraction',
        alias='@type',
        serialization_alias='@type'
    )
    touristType: Optional[Union["Audience", List["Audience"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'touristType',
            'https://schema.org/touristType'
        ),
        serialization_alias='https://schema.org/touristType'
    )
    availableLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
