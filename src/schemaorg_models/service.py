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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .audience import Audience
    from .aggregate_rating import AggregateRating
    from .review import Review
    from .service_channel import ServiceChannel
    from .category_code import CategoryCode
    from .organization import Organization
    from .image_object import ImageObject
    from .offer import Offer
    from .certification import Certification
    from .brand import Brand
    from .offer_catalog import OfferCatalog
    from .physical_activity_category import PhysicalActivityCategory
    from .opening_hours_specification import OpeningHoursSpecification
    from .geo_shape import GeoShape
    from .demand import Demand
    from .administrative_area import AdministrativeArea
    from .product import Product
    from .thing import Thing
    from .place import Place
    from .person import Person
    from .government_benefits_type import GovernmentBenefitsType

class Service(Intangible):
    """
A service provided by an organization, e.g. delivery service, print services, etc.
    """
    class_: Literal['https://schema.org/Service'] = Field( # type: ignore
        default='https://schema.org/Service',
        alias='@type',
        serialization_alias='@type'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'slogan',
            'https://schema.org/slogan'
        ),
        serialization_alias='https://schema.org/slogan'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    audience: Optional[Union["Audience", List["Audience"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audience',
            'https://schema.org/audience'
        ),
        serialization_alias='https://schema.org/audience'
    )
    produces: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'produces',
            'https://schema.org/produces'
        ),
        serialization_alias='https://schema.org/produces'
    )
    hoursAvailable: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hoursAvailable',
            'https://schema.org/hoursAvailable'
        ),
        serialization_alias='https://schema.org/hoursAvailable'
    )
    serviceAudience: Optional[Union["Audience", List["Audience"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceAudience',
            'https://schema.org/serviceAudience'
        ),
        serialization_alias='https://schema.org/serviceAudience'
    )
    termsOfService: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'termsOfService',
            'https://schema.org/termsOfService'
        ),
        serialization_alias='https://schema.org/termsOfService'
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'award',
            'https://schema.org/award'
        ),
        serialization_alias='https://schema.org/award'
    )
    availableChannel: Optional[Union["ServiceChannel", List["ServiceChannel"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableChannel',
            'https://schema.org/availableChannel'
        ),
        serialization_alias='https://schema.org/availableChannel'
    )
    isSimilarTo: Optional[Union["Service", List["Service"], "Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isSimilarTo',
            'https://schema.org/isSimilarTo'
        ),
        serialization_alias='https://schema.org/isSimilarTo'
    )
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    providerMobility: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'providerMobility',
            'https://schema.org/providerMobility'
        ),
        serialization_alias='https://schema.org/providerMobility'
    )
    brand: Optional[Union["Organization", List["Organization"], "Brand", List["Brand"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'brand',
            'https://schema.org/brand'
        ),
        serialization_alias='https://schema.org/brand'
    )
    review: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    broker: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broker',
            'https://schema.org/broker'
        ),
        serialization_alias='https://schema.org/broker'
    )
    provider: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], "Thing", List["Thing"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
    serviceArea: Optional[Union["AdministrativeArea", List["AdministrativeArea"], "GeoShape", List["GeoShape"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceArea',
            'https://schema.org/serviceArea'
        ),
        serialization_alias='https://schema.org/serviceArea'
    )
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOfferCatalog',
            'https://schema.org/hasOfferCatalog'
        ),
        serialization_alias='https://schema.org/hasOfferCatalog'
    )
    hasCertification: Optional[Union["Certification", List["Certification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification',
            'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification'
    )
    serviceType: Optional[Union["GovernmentBenefitsType", List["GovernmentBenefitsType"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceType',
            'https://schema.org/serviceType'
        ),
        serialization_alias='https://schema.org/serviceType'
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    areaServed: Optional[Union["GeoShape", List["GeoShape"], str, List[str], "AdministrativeArea", List["AdministrativeArea"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
    isRelatedTo: Optional[Union["Service", List["Service"], "Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isRelatedTo',
            'https://schema.org/isRelatedTo'
        ),
        serialization_alias='https://schema.org/isRelatedTo'
    )
    serviceOutput: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceOutput',
            'https://schema.org/serviceOutput'
        ),
        serialization_alias='https://schema.org/serviceOutput'
    )
