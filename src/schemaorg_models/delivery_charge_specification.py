from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.price_specification import PriceSpecification

from schemaorg_models.geo_shape import GeoShape
from schemaorg_models.administrative_area import AdministrativeArea
from schemaorg_models.place import Place
from schemaorg_models.delivery_method import DeliveryMethod

class DeliveryChargeSpecification(PriceSpecification):
    """
The price for the delivery of an offer using a particular delivery method.
    """
    type_: Literal['https://schema.org/DeliveryChargeSpecification'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DeliveryChargeSpecification'),serialization_alias='class') # type: ignore
    areaServed: Optional[Union[GeoShape, List[GeoShape], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),serialization_alias='https://schema.org/areaServed')
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape], str, List[str], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('eligibleRegion', 'https://schema.org/eligibleRegion'),serialization_alias='https://schema.org/eligibleRegion')
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None,validation_alias=AliasChoices('appliesToDeliveryMethod', 'https://schema.org/appliesToDeliveryMethod'),serialization_alias='https://schema.org/appliesToDeliveryMethod')
    ineligibleRegion: Optional[Union[str, List[str], Place, List[Place], GeoShape, List[GeoShape]]] = Field(default=None,validation_alias=AliasChoices('ineligibleRegion', 'https://schema.org/ineligibleRegion'),serialization_alias='https://schema.org/ineligibleRegion')
