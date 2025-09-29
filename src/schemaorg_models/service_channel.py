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
    from .contact_point import ContactPoint
    from .language import Language
    from .postal_address import PostalAddress
    from .duration import Duration
    from .service import Service
    from .place import Place

class ServiceChannel(Intangible):
    """
A means for accessing a service, e.g. a government office location, web site, or phone number.
    """
    class_: Literal['https://schema.org/ServiceChannel'] = Field( # type: ignore
        default='https://schema.org/ServiceChannel',
        alias='@type',
        serialization_alias='@type'
    )
    processingTime: Optional[Union["Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'processingTime',
            'https://schema.org/processingTime'
        ),
        serialization_alias='https://schema.org/processingTime'
    )
    availableLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
    servicePostalAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'servicePostalAddress',
            'https://schema.org/servicePostalAddress'
        ),
        serialization_alias='https://schema.org/servicePostalAddress'
    )
    providesService: Optional[Union["Service", List["Service"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'providesService',
            'https://schema.org/providesService'
        ),
        serialization_alias='https://schema.org/providesService'
    )
    serviceSmsNumber: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceSmsNumber',
            'https://schema.org/serviceSmsNumber'
        ),
        serialization_alias='https://schema.org/serviceSmsNumber'
    )
    serviceUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceUrl',
            'https://schema.org/serviceUrl'
        ),
        serialization_alias='https://schema.org/serviceUrl'
    )
    serviceLocation: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceLocation',
            'https://schema.org/serviceLocation'
        ),
        serialization_alias='https://schema.org/serviceLocation'
    )
    servicePhone: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'servicePhone',
            'https://schema.org/servicePhone'
        ),
        serialization_alias='https://schema.org/servicePhone'
    )
