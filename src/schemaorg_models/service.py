from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.audience import Audience
from schemaorg_models.thing import Thing
from schemaorg_models.product import Product
from schemaorg_models.organization import Organization
from schemaorg_models.brand import Brand
from schemaorg_models.person import Person
from schemaorg_models.administrative_area import AdministrativeArea
from schemaorg_models.place import Place

class Service(Intangible):
    """
A service provided by an organization, e.g. delivery service, print services, etc.
    """
    type_: Literal['https://schema.org/Service'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Service'),serialization_alias='class') # type: ignore
    slogan: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),serialization_alias='https://schema.org/slogan')
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(default=None,validation_alias=AliasChoices('logo', 'https://schema.org/logo'),serialization_alias='https://schema.org/logo')
    @field_serializer('logo')
    def logo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    audience: Optional[Union[Audience, List[Audience]]] = Field(default=None,validation_alias=AliasChoices('audience', 'https://schema.org/audience'),serialization_alias='https://schema.org/audience')
    produces: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('produces', 'https://schema.org/produces'),serialization_alias='https://schema.org/produces')
    hoursAvailable: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(default=None,validation_alias=AliasChoices('hoursAvailable', 'https://schema.org/hoursAvailable'),serialization_alias='https://schema.org/hoursAvailable')
    serviceAudience: Optional[Union[Audience, List[Audience]]] = Field(default=None,validation_alias=AliasChoices('serviceAudience', 'https://schema.org/serviceAudience'),serialization_alias='https://schema.org/serviceAudience')
    termsOfService: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('termsOfService', 'https://schema.org/termsOfService'),serialization_alias='https://schema.org/termsOfService')
    @field_serializer('termsOfService')
    def termsOfService2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    award: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('award', 'https://schema.org/award'),serialization_alias='https://schema.org/award')
    availableChannel: Optional[Union["ServiceChannel", List["ServiceChannel"]]] = Field(default=None,validation_alias=AliasChoices('availableChannel', 'https://schema.org/availableChannel'),serialization_alias='https://schema.org/availableChannel')
    isSimilarTo: Optional[Union["Service", List["Service"], Product, List[Product]]] = Field(default=None,validation_alias=AliasChoices('isSimilarTo', 'https://schema.org/isSimilarTo'),serialization_alias='https://schema.org/isSimilarTo')
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(default=None,validation_alias=AliasChoices('offers', 'https://schema.org/offers'),serialization_alias='https://schema.org/offers')
    providerMobility: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('providerMobility', 'https://schema.org/providerMobility'),serialization_alias='https://schema.org/providerMobility')
    brand: Optional[Union[Organization, List[Organization], Brand, List[Brand]]] = Field(default=None,validation_alias=AliasChoices('brand', 'https://schema.org/brand'),serialization_alias='https://schema.org/brand')
    review: Optional[Union["Review", List["Review"]]] = Field(default=None,validation_alias=AliasChoices('review', 'https://schema.org/review'),serialization_alias='https://schema.org/review')
    broker: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('broker', 'https://schema.org/broker'),serialization_alias='https://schema.org/broker')
    provider: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('provider', 'https://schema.org/provider'),serialization_alias='https://schema.org/provider')
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('category', 'https://schema.org/category'),serialization_alias='https://schema.org/category')
    @field_serializer('category')
    def category2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    serviceArea: Optional[Union[AdministrativeArea, List[AdministrativeArea], "GeoShape", List["GeoShape"], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('serviceArea', 'https://schema.org/serviceArea'),serialization_alias='https://schema.org/serviceArea')
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = Field(default=None,validation_alias=AliasChoices('hasOfferCatalog', 'https://schema.org/hasOfferCatalog'),serialization_alias='https://schema.org/hasOfferCatalog')
    hasCertification: Optional[Union["Certification", List["Certification"]]] = Field(default=None,validation_alias=AliasChoices('hasCertification', 'https://schema.org/hasCertification'),serialization_alias='https://schema.org/hasCertification')
    serviceType: Optional[Union["GovernmentBenefitsType", List["GovernmentBenefitsType"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('serviceType', 'https://schema.org/serviceType'),serialization_alias='https://schema.org/serviceType')
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(default=None,validation_alias=AliasChoices('aggregateRating', 'https://schema.org/aggregateRating'),serialization_alias='https://schema.org/aggregateRating')
    areaServed: Optional[Union["GeoShape", List["GeoShape"], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),serialization_alias='https://schema.org/areaServed')
    isRelatedTo: Optional[Union["Service", List["Service"], Product, List[Product]]] = Field(default=None,validation_alias=AliasChoices('isRelatedTo', 'https://schema.org/isRelatedTo'),serialization_alias='https://schema.org/isRelatedTo')
    serviceOutput: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('serviceOutput', 'https://schema.org/serviceOutput'),serialization_alias='https://schema.org/serviceOutput')
