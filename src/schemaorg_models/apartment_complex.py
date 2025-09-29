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
from .residence import Residence
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class ApartmentComplex(Residence):
    '''
    Residence type: Apartment complex.

    Attributes:
        tourBookingPage: A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        numberOfAvailableAccommodationUnits: Indicates the number of available accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].
        numberOfBedrooms: The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].
        petsAllowed: Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        numberOfAccommodationUnits: Indicates the total (available plus unavailable) number of accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].
    '''
    class_: Literal['https://schema.org/ApartmentComplex'] = Field( # type: ignore
        default='https://schema.org/ApartmentComplex',
        alias='@type',
        serialization_alias='@type'
    )
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tourBookingPage',
            'https://schema.org/tourBookingPage'
        ),
        serialization_alias='https://schema.org/tourBookingPage'
    )
    numberOfAvailableAccommodationUnits: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfAvailableAccommodationUnits',
            'https://schema.org/numberOfAvailableAccommodationUnits'
        ),
        serialization_alias='https://schema.org/numberOfAvailableAccommodationUnits'
    )
    numberOfBedrooms: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfBedrooms',
            'https://schema.org/numberOfBedrooms'
        ),
        serialization_alias='https://schema.org/numberOfBedrooms'
    )
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'petsAllowed',
            'https://schema.org/petsAllowed'
        ),
        serialization_alias='https://schema.org/petsAllowed'
    )
    numberOfAccommodationUnits: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfAccommodationUnits',
            'https://schema.org/numberOfAccommodationUnits'
        ),
        serialization_alias='https://schema.org/numberOfAccommodationUnits'
    )
