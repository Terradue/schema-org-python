from __future__ import annotations
from datetime import (
    datetime,
    time
)
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
from .local_business import LocalBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .audience import Audience
    from .rating import Rating
    from .language import Language
    from .location_feature_specification import LocationFeatureSpecification
    from .quantitative_value import QuantitativeValue

class LodgingBusiness(LocalBusiness):
    """
A lodging business, such as a motel, hotel, or inn.
    """
    class_: Literal['https://schema.org/LodgingBusiness'] = Field( # type: ignore
        default='https://schema.org/LodgingBusiness',
        alias='@type',
        serialization_alias='@type'
    )
    amenityFeature: Optional[Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature',
            'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature'
    )
    audience: Optional[Union["Audience", List["Audience"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audience',
            'https://schema.org/audience'
        ),
        serialization_alias='https://schema.org/audience'
    )
    checkoutTime: Optional[Union[datetime, List[datetime], time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'checkoutTime',
            'https://schema.org/checkoutTime'
        ),
        serialization_alias='https://schema.org/checkoutTime'
    )
    numberOfRooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfRooms',
            'https://schema.org/numberOfRooms'
        ),
        serialization_alias='https://schema.org/numberOfRooms'
    )
    starRating: Optional[Union["Rating", List["Rating"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'starRating',
            'https://schema.org/starRating'
        ),
        serialization_alias='https://schema.org/starRating'
    )
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'petsAllowed',
            'https://schema.org/petsAllowed'
        ),
        serialization_alias='https://schema.org/petsAllowed'
    )
    availableLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
    checkinTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'checkinTime',
            'https://schema.org/checkinTime'
        ),
        serialization_alias='https://schema.org/checkinTime'
    )
