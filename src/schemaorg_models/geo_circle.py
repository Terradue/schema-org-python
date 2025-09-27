from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.geo_shape import GeoShape

from schemaorg_models.geo_coordinates import GeoCoordinates
from schemaorg_models.distance import Distance

class GeoCircle(GeoShape):
    """
A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape
          it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.
          The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'.
       
    """
    class_: Literal['https://schema.org/GeoCircle'] = Field(default='https://schema.org/GeoCircle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    geoMidpoint: Optional[Union[GeoCoordinates, List[GeoCoordinates]]] = Field(default=None, validation_alias=AliasChoices('geoMidpoint', 'https://schema.org/geoMidpoint'), serialization_alias='https://schema.org/geoMidpoint')
    geoRadius: Optional[Union[float, List[float], Distance, List[Distance], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('geoRadius', 'https://schema.org/geoRadius'), serialization_alias='https://schema.org/geoRadius')
