from __future__ import annotations
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
from .place import Place
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .floor_plan import FloorPlan
    from .duration import Duration
    from .bed_type import BedType
    from .bed_details import BedDetails
    from .location_feature_specification import LocationFeatureSpecification

class Accommodation(Place):
    """
An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.
For more specific types of accommodations not defined in schema.org, one can use [[additionalType]] with external vocabularies.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/Accommodation'] = Field( # type: ignore
        default='https://schema.org/Accommodation',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfRooms: Optional[Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfRooms',
            'https://schema.org/numberOfRooms'
        ),
        serialization_alias='https://schema.org/numberOfRooms'
    )
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'petsAllowed',
            'https://schema.org/petsAllowed'
        ),
        serialization_alias='https://schema.org/petsAllowed'
    )
    numberOfBathroomsTotal: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfBathroomsTotal',
            'https://schema.org/numberOfBathroomsTotal'
        ),
        serialization_alias='https://schema.org/numberOfBathroomsTotal'
    )
    leaseLength: Optional[Union[QuantitativeValue, List[QuantitativeValue], Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'leaseLength',
            'https://schema.org/leaseLength'
        ),
        serialization_alias='https://schema.org/leaseLength'
    )
    numberOfBedrooms: Optional[Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfBedrooms',
            'https://schema.org/numberOfBedrooms'
        ),
        serialization_alias='https://schema.org/numberOfBedrooms'
    )
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accommodationFloorPlan',
            'https://schema.org/accommodationFloorPlan'
        ),
        serialization_alias='https://schema.org/accommodationFloorPlan'
    )
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfFullBathrooms',
            'https://schema.org/numberOfFullBathrooms'
        ),
        serialization_alias='https://schema.org/numberOfFullBathrooms'
    )
    floorLevel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'floorLevel',
            'https://schema.org/floorLevel'
        ),
        serialization_alias='https://schema.org/floorLevel'
    )
    floorSize: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'floorSize',
            'https://schema.org/floorSize'
        ),
        serialization_alias='https://schema.org/floorSize'
    )
    accommodationCategory: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accommodationCategory',
            'https://schema.org/accommodationCategory'
        ),
        serialization_alias='https://schema.org/accommodationCategory'
    )
    amenityFeature: Optional[Union[LocationFeatureSpecification, List[LocationFeatureSpecification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature',
            'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature'
    )
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tourBookingPage',
            'https://schema.org/tourBookingPage'
        ),
        serialization_alias='https://schema.org/tourBookingPage'
    )
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupancy',
            'https://schema.org/occupancy'
        ),
        serialization_alias='https://schema.org/occupancy'
    )
    permittedUsage: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'permittedUsage',
            'https://schema.org/permittedUsage'
        ),
        serialization_alias='https://schema.org/permittedUsage'
    )
    bed: Optional[Union[BedType, List[BedType], str, List[str], BedDetails, List[BedDetails]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bed',
            'https://schema.org/bed'
        ),
        serialization_alias='https://schema.org/bed'
    )
    yearBuilt: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'yearBuilt',
            'https://schema.org/yearBuilt'
        ),
        serialization_alias='https://schema.org/yearBuilt'
    )
    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPartialBathrooms',
            'https://schema.org/numberOfPartialBathrooms'
        ),
        serialization_alias='https://schema.org/numberOfPartialBathrooms'
    )
