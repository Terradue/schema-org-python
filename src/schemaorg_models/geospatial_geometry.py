from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.place import Place

class GeospatialGeometry(Intangible):
    """
(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.
    """
    class_: Literal['https://schema.org/GeospatialGeometry'] = Field(default='https://schema.org/GeospatialGeometry', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    geoCoveredBy: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('geoCoveredBy', 'https://schema.org/geoCoveredBy'), serialization_alias='https://schema.org/geoCoveredBy')
    geoEquals: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoEquals', 'https://schema.org/geoEquals'), serialization_alias='https://schema.org/geoEquals')
    geoCovers: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoCovers', 'https://schema.org/geoCovers'), serialization_alias='https://schema.org/geoCovers')
    geoOverlaps: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoOverlaps', 'https://schema.org/geoOverlaps'), serialization_alias='https://schema.org/geoOverlaps')
    geoContains: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoContains', 'https://schema.org/geoContains'), serialization_alias='https://schema.org/geoContains')
    geoDisjoint: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('geoDisjoint', 'https://schema.org/geoDisjoint'), serialization_alias='https://schema.org/geoDisjoint')
    geoWithin: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('geoWithin', 'https://schema.org/geoWithin'), serialization_alias='https://schema.org/geoWithin')
    geoTouches: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoTouches', 'https://schema.org/geoTouches'), serialization_alias='https://schema.org/geoTouches')
    geoCrosses: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoCrosses', 'https://schema.org/geoCrosses'), serialization_alias='https://schema.org/geoCrosses')
    geoIntersects: Optional[Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]] = Field(default=None, validation_alias=AliasChoices('geoIntersects', 'https://schema.org/geoIntersects'), serialization_alias='https://schema.org/geoIntersects')
