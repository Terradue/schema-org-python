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
    from .review import Review
    from .certification import Certification
    from .geo_shape import GeoShape
    from .geospatial_geometry import GeospatialGeometry
    from .event import Event
    from .image_object import ImageObject
    from .defined_term import DefinedTerm
    from .opening_hours_specification import OpeningHoursSpecification
    from .map import Map
    from .location_feature_specification import LocationFeatureSpecification
    from .property_value import PropertyValue
    from .aggregate_rating import AggregateRating
    from .postal_address import PostalAddress
    from .photograph import Photograph
    from .geo_coordinates import GeoCoordinates

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    globalLocationNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    event: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasCertification: Optional[Union['Certification', List['Certification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoIntersects: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoCoveredBy: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    reviews: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasMap: Optional[Union[HttpUrl, List[HttpUrl], 'Map', List['Map']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    longitude: Optional[Union[float, List[float], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    photos: Optional[Union['Photograph', List['Photograph'], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    photo: Optional[Union['Photograph', List['Photograph'], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoEquals: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasDriveThroughService: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoCovers: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    amenityFeature: Optional[Union['LocationFeatureSpecification', List['LocationFeatureSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    map: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geo: Optional[Union['GeoShape', List['GeoShape'], 'GeoCoordinates', List['GeoCoordinates']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    latitude: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    publicAccess: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maps: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    branchCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    address: Optional[Union[str, List[str], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    events: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    openingHoursSpecification: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoContains: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    smokingAllowed: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoDisjoint: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    containedInPlace: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoOverlaps: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    containedIn: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    specialOpeningHoursSpecification: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoTouches: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    containsPlace: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isicV4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoCrosses: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    geoWithin: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
