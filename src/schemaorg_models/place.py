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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .photograph import Photograph
    from .image_object import ImageObject
    from .geo_shape import GeoShape
    from .opening_hours_specification import OpeningHoursSpecification
    from .defined_term import DefinedTerm
    from .property_value import PropertyValue
    from .geospatial_geometry import GeospatialGeometry
    from .location_feature_specification import LocationFeatureSpecification
    from .review import Review
    from .event import Event
    from .certification import Certification
    from .postal_address import PostalAddress
    from .geo_coordinates import GeoCoordinates
    from .map import Map
    from .aggregate_rating import AggregateRating

class Place(Thing):
    '''
    Entities that have a somewhat fixed, physical extension.

    Attributes:
        faxNumber: The fax number.
        globalLocationNumber: The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        event: Upcoming or past event associated with this place, organization, or action.
        hasCertification: Certification information about a product, organization, service, place, or person.
        isAccessibleForFree: A flag to signal that the item, event, or place is accessible for free.
        geoIntersects: Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoCoveredBy: Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        reviews: Review of the item.
        aggregateRating: The overall rating, based on a collection of reviews or ratings, of the item.
        hasMap: A URL to a map of the place.
        longitude: The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        photos: Photographs of this place.
        photo: A photograph of this place.
        geoEquals: Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).
        hasDriveThroughService: Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]]) offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]] such facilities could potentially help with social distancing from other potentially-infected users.
        geoCovers: Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        slogan: A slogan or motto associated with the item.
        amenityFeature: An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        keywords: Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        logo: An associated logo.
        map: A URL to a map of the place.
        geo: The geo coordinates of the place.
        tourBookingPage: A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        latitude: The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        publicAccess: A flag to signal that the [[Place]] is open to public visitors.  If this property is omitted there is no assumed default boolean value.
        maps: A URL to a map of the place.
        branchCode: A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs.\
\
For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.
      
        address: Physical address of the item.
        additionalProperty: A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\
\
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

        events: Upcoming or past events associated with this place or organization.
        openingHoursSpecification: The opening hours of a certain place.
        hasGS1DigitalLink: The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>)  should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly.
        geoContains: Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        telephone: The telephone number.
        smokingAllowed: Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.
        geoDisjoint: Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set of disconnected geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        containedInPlace: The basic containment relation between a place and one that contains it.
        geoOverlaps: Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        review: A review of the item.
        containedIn: The basic containment relation between a place and one that contains it.
        specialOpeningHoursSpecification: The special opening hours of a certain place.\
\
Use this to explicitly override general opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].
      
        geoTouches: Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        containsPlace: The basic containment relation between a place and another that it contains.
        isicV4: The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        geoCrosses: Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        maximumAttendeeCapacity: The total number of individuals that may attend an event or venue.
        geoWithin: Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
    '''
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
    event: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
    hasCertification: Optional[Union['Certification', List['Certification']]] = Field(
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
    geoIntersects: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoIntersects',
            'https://schema.org/geoIntersects'
        ),
        serialization_alias='https://schema.org/geoIntersects'
    )
    geoCoveredBy: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCoveredBy',
            'https://schema.org/geoCoveredBy'
        ),
        serialization_alias='https://schema.org/geoCoveredBy'
    )
    reviews: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    hasMap: Optional[Union[HttpUrl, List[HttpUrl], 'Map', List['Map']]] = Field(
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
    photos: Optional[Union['Photograph', List['Photograph'], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'photos',
            'https://schema.org/photos'
        ),
        serialization_alias='https://schema.org/photos'
    )
    photo: Optional[Union['Photograph', List['Photograph'], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'photo',
            'https://schema.org/photo'
        ),
        serialization_alias='https://schema.org/photo'
    )
    geoEquals: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
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
    geoCovers: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
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
    amenityFeature: Optional[Union['LocationFeatureSpecification', List['LocationFeatureSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature',
            'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
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
    geo: Optional[Union['GeoShape', List['GeoShape'], 'GeoCoordinates', List['GeoCoordinates']]] = Field(
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
    address: Optional[Union[str, List[str], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'address',
            'https://schema.org/address'
        ),
        serialization_alias='https://schema.org/address'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    events: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'events',
            'https://schema.org/events'
        ),
        serialization_alias='https://schema.org/events'
    )
    openingHoursSpecification: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
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
    geoContains: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
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
    geoDisjoint: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoDisjoint',
            'https://schema.org/geoDisjoint'
        ),
        serialization_alias='https://schema.org/geoDisjoint'
    )
    containedInPlace: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containedInPlace',
            'https://schema.org/containedInPlace'
        ),
        serialization_alias='https://schema.org/containedInPlace'
    )
    geoOverlaps: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoOverlaps',
            'https://schema.org/geoOverlaps'
        ),
        serialization_alias='https://schema.org/geoOverlaps'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    containedIn: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containedIn',
            'https://schema.org/containedIn'
        ),
        serialization_alias='https://schema.org/containedIn'
    )
    specialOpeningHoursSpecification: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'specialOpeningHoursSpecification',
            'https://schema.org/specialOpeningHoursSpecification'
        ),
        serialization_alias='https://schema.org/specialOpeningHoursSpecification'
    )
    geoTouches: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoTouches',
            'https://schema.org/geoTouches'
        ),
        serialization_alias='https://schema.org/geoTouches'
    )
    containsPlace: Optional[Union['Place', List['Place']]] = Field(
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
    geoCrosses: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
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
    geoWithin: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoWithin',
            'https://schema.org/geoWithin'
        ),
        serialization_alias='https://schema.org/geoWithin'
    )
