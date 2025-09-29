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
    from .place import Place

class GeospatialGeometry(Intangible):
    '''
    (Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.

    Attributes:
        geoCoveredBy: Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoEquals: Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).
        geoCovers: Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoOverlaps: Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoContains: Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoDisjoint: Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set of disconnected geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoWithin: Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoTouches: Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoCrosses: Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoIntersects: Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
    '''
    class_: Literal['https://schema.org/GeospatialGeometry'] = Field( # type: ignore
        default='https://schema.org/GeospatialGeometry',
        alias='@type',
        serialization_alias='@type'
    )
    geoCoveredBy: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCoveredBy',
            'https://schema.org/geoCoveredBy'
        ),
        serialization_alias='https://schema.org/geoCoveredBy'
    )
    geoEquals: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoEquals',
            'https://schema.org/geoEquals'
        ),
        serialization_alias='https://schema.org/geoEquals'
    )
    geoCovers: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCovers',
            'https://schema.org/geoCovers'
        ),
        serialization_alias='https://schema.org/geoCovers'
    )
    geoOverlaps: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoOverlaps',
            'https://schema.org/geoOverlaps'
        ),
        serialization_alias='https://schema.org/geoOverlaps'
    )
    geoContains: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoContains',
            'https://schema.org/geoContains'
        ),
        serialization_alias='https://schema.org/geoContains'
    )
    geoDisjoint: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoDisjoint',
            'https://schema.org/geoDisjoint'
        ),
        serialization_alias='https://schema.org/geoDisjoint'
    )
    geoWithin: Optional[Union['GeospatialGeometry', List['GeospatialGeometry'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoWithin',
            'https://schema.org/geoWithin'
        ),
        serialization_alias='https://schema.org/geoWithin'
    )
    geoTouches: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoTouches',
            'https://schema.org/geoTouches'
        ),
        serialization_alias='https://schema.org/geoTouches'
    )
    geoCrosses: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCrosses',
            'https://schema.org/geoCrosses'
        ),
        serialization_alias='https://schema.org/geoCrosses'
    )
    geoIntersects: Optional[Union['Place', List['Place'], 'GeospatialGeometry', List['GeospatialGeometry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoIntersects',
            'https://schema.org/geoIntersects'
        ),
        serialization_alias='https://schema.org/geoIntersects'
    )
