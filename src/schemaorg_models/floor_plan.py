from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.accommodation import Accommodation

class FloorPlan(Intangible):
    """
A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]]. 
    """
    class_: Literal['https://schema.org/FloorPlan'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    numberOfAvailableAccommodationUnits: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfAvailableAccommodationUnits', 'https://schema.org/numberOfAvailableAccommodationUnits'), serialization_alias='https://schema.org/numberOfAvailableAccommodationUnits')
    layoutImage: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(default=None,validation_alias=AliasChoices('layoutImage', 'https://schema.org/layoutImage'), serialization_alias='https://schema.org/layoutImage')
    @field_serializer('layoutImage')
    def layoutImage2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('numberOfPartialBathrooms', 'https://schema.org/numberOfPartialBathrooms'), serialization_alias='https://schema.org/numberOfPartialBathrooms')
    numberOfBedrooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfBedrooms', 'https://schema.org/numberOfBedrooms'), serialization_alias='https://schema.org/numberOfBedrooms')
    numberOfRooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfRooms', 'https://schema.org/numberOfRooms'), serialization_alias='https://schema.org/numberOfRooms')
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('petsAllowed', 'https://schema.org/petsAllowed'), serialization_alias='https://schema.org/petsAllowed')
    numberOfBathroomsTotal: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numberOfBathroomsTotal', 'https://schema.org/numberOfBathroomsTotal'), serialization_alias='https://schema.org/numberOfBathroomsTotal')
    numberOfAccommodationUnits: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfAccommodationUnits', 'https://schema.org/numberOfAccommodationUnits'), serialization_alias='https://schema.org/numberOfAccommodationUnits')
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('numberOfFullBathrooms', 'https://schema.org/numberOfFullBathrooms'), serialization_alias='https://schema.org/numberOfFullBathrooms')
    floorSize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('floorSize', 'https://schema.org/floorSize'), serialization_alias='https://schema.org/floorSize')
    isPlanForApartment: Optional[Union[Accommodation, List[Accommodation]]] = Field(default=None,validation_alias=AliasChoices('isPlanForApartment', 'https://schema.org/isPlanForApartment'), serialization_alias='https://schema.org/isPlanForApartment')
    amenityFeature: Optional[Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]] = Field(default=None,validation_alias=AliasChoices('amenityFeature', 'https://schema.org/amenityFeature'), serialization_alias='https://schema.org/amenityFeature')
