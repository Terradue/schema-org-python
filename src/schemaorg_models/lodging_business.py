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
from .local_business import LocalBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rating import Rating
    from .quantitative_value import QuantitativeValue
    from .audience import Audience
    from .language import Language
    from .location_feature_specification import LocationFeatureSpecification

class LodgingBusiness(LocalBusiness):
    '''
    A lodging business, such as a motel, hotel, or inn.

    Attributes:
        amenityFeature: An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        audience: An intended audience, i.e. a group for whom something was created.
        checkoutTime: The latest someone may check out of a lodging establishment.
        numberOfRooms: The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        starRating: An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        petsAllowed: Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        availableLanguage: A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        checkinTime: The earliest someone may check into a lodging establishment.
    '''
    class_: Literal['https://schema.org/LodgingBusiness'] = Field( # type: ignore
        default='https://schema.org/LodgingBusiness',
        alias='@type',
        serialization_alias='@type'
    )
    amenityFeature: Optional[Union['LocationFeatureSpecification', List['LocationFeatureSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature',
            'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature'
    )
    audience: Optional[Union['Audience', List['Audience']]] = Field(
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
    numberOfRooms: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfRooms',
            'https://schema.org/numberOfRooms'
        ),
        serialization_alias='https://schema.org/numberOfRooms'
    )
    starRating: Optional[Union['Rating', List['Rating']]] = Field(
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
    availableLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
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
