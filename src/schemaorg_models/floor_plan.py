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
    from .image_object import ImageObject
    from .accommodation import Accommodation
    from .location_feature_specification import LocationFeatureSpecification
    from .quantitative_value import QuantitativeValue

class FloorPlan(Intangible):
    '''
    A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]]. 

    Attributes:
        numberOfAvailableAccommodationUnits: Indicates the number of available accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].
        layoutImage: A schematic image showing the floorplan layout.
        numberOfPartialBathrooms: Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field). 
        numberOfBedrooms: The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].
        numberOfRooms: The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        petsAllowed: Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        numberOfBathroomsTotal: The total integer number of bathrooms in some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]].
        numberOfAccommodationUnits: Indicates the total (available plus unavailable) number of accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].
        numberOfFullBathrooms: Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).
        floorSize: The size of the accommodation, e.g. in square meter or squarefoot.
Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard.
        isPlanForApartment: Indicates some accommodation that this floor plan describes.
        amenityFeature: An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
    '''
    class_: Literal['https://schema.org/FloorPlan'] = Field( # type: ignore
        default='https://schema.org/FloorPlan',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfAvailableAccommodationUnits: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfAvailableAccommodationUnits',
            'https://schema.org/numberOfAvailableAccommodationUnits'
        ),
        serialization_alias='https://schema.org/numberOfAvailableAccommodationUnits'
    )
    layoutImage: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'layoutImage',
            'https://schema.org/layoutImage'
        ),
        serialization_alias='https://schema.org/layoutImage'
    )
    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPartialBathrooms',
            'https://schema.org/numberOfPartialBathrooms'
        ),
        serialization_alias='https://schema.org/numberOfPartialBathrooms'
    )
    numberOfBedrooms: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfBedrooms',
            'https://schema.org/numberOfBedrooms'
        ),
        serialization_alias='https://schema.org/numberOfBedrooms'
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
    numberOfAccommodationUnits: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfAccommodationUnits',
            'https://schema.org/numberOfAccommodationUnits'
        ),
        serialization_alias='https://schema.org/numberOfAccommodationUnits'
    )
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfFullBathrooms',
            'https://schema.org/numberOfFullBathrooms'
        ),
        serialization_alias='https://schema.org/numberOfFullBathrooms'
    )
    floorSize: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'floorSize',
            'https://schema.org/floorSize'
        ),
        serialization_alias='https://schema.org/floorSize'
    )
    isPlanForApartment: Optional[Union['Accommodation', List['Accommodation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isPlanForApartment',
            'https://schema.org/isPlanForApartment'
        ),
        serialization_alias='https://schema.org/isPlanForApartment'
    )
    amenityFeature: Optional[Union['LocationFeatureSpecification', List['LocationFeatureSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature',
            'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature'
    )
