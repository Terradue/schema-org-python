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
    from .contact_point import ContactPoint
    from .service import Service
    from .place import Place
    from .language import Language
    from .duration import Duration
    from .postal_address import PostalAddress

class ServiceChannel(Intangible):
    '''
    A means for accessing a service, e.g. a government office location, web site, or phone number.

    Attributes:
        processingTime: Estimated processing time for the service using this channel.
        availableLanguage: A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        servicePostalAddress: The address for accessing the service by mail.
        providesService: The service provided by this channel.
        serviceSmsNumber: The number to access the service by text message.
        serviceUrl: The website to access the service.
        serviceLocation: The location (e.g. civic structure, local business, etc.) where a person can go to access the service.
        servicePhone: The phone number to use to access the service.
    '''
    class_: Literal['https://schema.org/ServiceChannel'] = Field( # type: ignore
        default='https://schema.org/ServiceChannel',
        alias='@type',
        serialization_alias='@type'
    )
    processingTime: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    availableLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    servicePostalAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    providesService: Optional[Union['Service', List['Service']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    serviceSmsNumber: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    serviceUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    serviceLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    servicePhone: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
