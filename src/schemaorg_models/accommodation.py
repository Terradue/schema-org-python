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
from .place import Place
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .bed_details import BedDetails
    from .duration import Duration
    from .floor_plan import FloorPlan
    from .bed_type import BedType
    from .location_feature_specification import LocationFeatureSpecification

class Accommodation(Place):
    '''
    An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.
For more specific types of accommodations not defined in schema.org, one can use [[additionalType]] with external vocabularies.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.


    Attributes:
        numberOfRooms: The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        petsAllowed: Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        numberOfBathroomsTotal: The total integer number of bathrooms in some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]].
        leaseLength: Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        numberOfBedrooms: The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].
        accommodationFloorPlan: A floorplan of some [[Accommodation]].
        numberOfFullBathrooms: Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).
        floorLevel: The floor level for an [[Accommodation]] in a multi-storey building. Since counting
  systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.
        floorSize: The size of the accommodation, e.g. in square meter or squarefoot.
Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard.
        accommodationCategory: Category of an [[Accommodation]], following real estate conventions, e.g. RESO (see [PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field) fields  for suggested values).
        amenityFeature: An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        tourBookingPage: A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        occupancy: The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).
Typical unit code(s): C62 for person.
        permittedUsage: Indications regarding the permitted usage of the accommodation.
        bed: The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text.
      If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property.
        yearBuilt: The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field). 
        numberOfPartialBathrooms: Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field). 
    '''
    class_: Literal['https://schema.org/Accommodation'] = Field( # type: ignore
        default='https://schema.org/Accommodation',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfRooms: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    leaseLength: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'leaseLength',
            'https://schema.org/leaseLength'
        ),
        serialization_alias='https://schema.org/leaseLength'
    )
    numberOfBedrooms: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfBedrooms',
            'https://schema.org/numberOfBedrooms'
        ),
        serialization_alias='https://schema.org/numberOfBedrooms'
    )
    accommodationFloorPlan: Optional[Union['FloorPlan', List['FloorPlan']]] = Field(
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
    floorSize: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    amenityFeature: Optional[Union['LocationFeatureSpecification', List['LocationFeatureSpecification']]] = Field(
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
    occupancy: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    bed: Optional[Union['BedType', List['BedType'], str, List[str], 'BedDetails', List['BedDetails']]] = Field(
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
