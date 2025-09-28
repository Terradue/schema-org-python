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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .location_feature_specification import LocationFeatureSpecification
    from .geospatial_geometry import GeospatialGeometry
    from .postal_address import PostalAddress
    from .aggregate_rating import AggregateRating
    from .photograph import Photograph
    from .geo_shape import GeoShape
    from .property_value import PropertyValue
    from .certification import Certification
    from .defined_term import DefinedTerm
    from .geo_coordinates import GeoCoordinates
    from .review import Review
    from .opening_hours_specification import OpeningHoursSpecification
    from .map import Map
    from .image_object import ImageObject
    from .event import Event

class Place(Thing):
    """
Entities that have a somewhat fixed, physical extension.
    """
    class_: Literal['https://schema.org/Place'] = Field( # type: ignore
        default='https://schema.org/Place',
        alias='@type',
        serialization_alias='@type'
    )
    faxNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'faxNumber',
            'https://schema.org/faxNumber'
        ),
        serialization_alias='https://schema.org/faxNumber'
    )
    globalLocationNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'globalLocationNumber',
            'https://schema.org/globalLocationNumber'
        ),
        serialization_alias='https://schema.org/globalLocationNumber'
    )
    event: Optional[Union["Event", List["Event"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
    hasCertification: Optional[Union["Certification", List["Certification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification',
            'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification'
    )
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessibleForFree',
            'https://schema.org/isAccessibleForFree'
        ),
        serialization_alias='https://schema.org/isAccessibleForFree'
    )
    geoIntersects: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoIntersects',
            'https://schema.org/geoIntersects'
        ),
        serialization_alias='https://schema.org/geoIntersects'
    )
    geoCoveredBy: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCoveredBy',
            'https://schema.org/geoCoveredBy'
        ),
        serialization_alias='https://schema.org/geoCoveredBy'
    )
    reviews: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    hasMap: Optional[Union[HttpUrl, List[HttpUrl], "Map", List["Map"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMap',
            'https://schema.org/hasMap'
        ),
        serialization_alias='https://schema.org/hasMap'
    )
    longitude: Optional[Union[float, List[float], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'longitude',
            'https://schema.org/longitude'
        ),
        serialization_alias='https://schema.org/longitude'
    )
    photos: Optional[Union["Photograph", List["Photograph"], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'photos',
            'https://schema.org/photos'
        ),
        serialization_alias='https://schema.org/photos'
    )
    photo: Optional[Union["Photograph", List["Photograph"], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'photo',
            'https://schema.org/photo'
        ),
        serialization_alias='https://schema.org/photo'
    )
    geoEquals: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoEquals',
            'https://schema.org/geoEquals'
        ),
        serialization_alias='https://schema.org/geoEquals'
    )
    hasDriveThroughService: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDriveThroughService',
            'https://schema.org/hasDriveThroughService'
        ),
        serialization_alias='https://schema.org/hasDriveThroughService'
    )
    geoCovers: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCovers',
            'https://schema.org/geoCovers'
        ),
        serialization_alias='https://schema.org/geoCovers'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'slogan',
            'https://schema.org/slogan'
        ),
        serialization_alias='https://schema.org/slogan'
    )
    amenityFeature: Optional[Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature',
            'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    map: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'map',
            'https://schema.org/map'
        ),
        serialization_alias='https://schema.org/map'
    )
    geo: Optional[Union["GeoShape", List["GeoShape"], "GeoCoordinates", List["GeoCoordinates"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geo',
            'https://schema.org/geo'
        ),
        serialization_alias='https://schema.org/geo'
    )
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tourBookingPage',
            'https://schema.org/tourBookingPage'
        ),
        serialization_alias='https://schema.org/tourBookingPage'
    )
    latitude: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'latitude',
            'https://schema.org/latitude'
        ),
        serialization_alias='https://schema.org/latitude'
    )
    publicAccess: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publicAccess',
            'https://schema.org/publicAccess'
        ),
        serialization_alias='https://schema.org/publicAccess'
    )
    maps: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maps',
            'https://schema.org/maps'
        ),
        serialization_alias='https://schema.org/maps'
    )
    branchCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'branchCode',
            'https://schema.org/branchCode'
        ),
        serialization_alias='https://schema.org/branchCode'
    )
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'address',
            'https://schema.org/address'
        ),
        serialization_alias='https://schema.org/address'
    )
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    events: Optional[Union["Event", List["Event"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'events',
            'https://schema.org/events'
        ),
        serialization_alias='https://schema.org/events'
    )
    openingHoursSpecification: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'openingHoursSpecification',
            'https://schema.org/openingHoursSpecification'
        ),
        serialization_alias='https://schema.org/openingHoursSpecification'
    )
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink',
            'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink'
    )
    geoContains: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoContains',
            'https://schema.org/geoContains'
        ),
        serialization_alias='https://schema.org/geoContains'
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'telephone',
            'https://schema.org/telephone'
        ),
        serialization_alias='https://schema.org/telephone'
    )
    smokingAllowed: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'smokingAllowed',
            'https://schema.org/smokingAllowed'
        ),
        serialization_alias='https://schema.org/smokingAllowed'
    )
    geoDisjoint: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoDisjoint',
            'https://schema.org/geoDisjoint'
        ),
        serialization_alias='https://schema.org/geoDisjoint'
    )
    containedInPlace: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containedInPlace',
            'https://schema.org/containedInPlace'
        ),
        serialization_alias='https://schema.org/containedInPlace'
    )
    geoOverlaps: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoOverlaps',
            'https://schema.org/geoOverlaps'
        ),
        serialization_alias='https://schema.org/geoOverlaps'
    )
    review: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    containedIn: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containedIn',
            'https://schema.org/containedIn'
        ),
        serialization_alias='https://schema.org/containedIn'
    )
    specialOpeningHoursSpecification: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'specialOpeningHoursSpecification',
            'https://schema.org/specialOpeningHoursSpecification'
        ),
        serialization_alias='https://schema.org/specialOpeningHoursSpecification'
    )
    geoTouches: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoTouches',
            'https://schema.org/geoTouches'
        ),
        serialization_alias='https://schema.org/geoTouches'
    )
    containsPlace: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containsPlace',
            'https://schema.org/containsPlace'
        ),
        serialization_alias='https://schema.org/containsPlace'
    )
    isicV4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isicV4',
            'https://schema.org/isicV4'
        ),
        serialization_alias='https://schema.org/isicV4'
    )
    geoCrosses: Optional[Union["Place", List["Place"], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCrosses',
            'https://schema.org/geoCrosses'
        ),
        serialization_alias='https://schema.org/geoCrosses'
    )
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumAttendeeCapacity',
            'https://schema.org/maximumAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/maximumAttendeeCapacity'
    )
    geoWithin: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoWithin',
            'https://schema.org/geoWithin'
        ),
        serialization_alias='https://schema.org/geoWithin'
    )
