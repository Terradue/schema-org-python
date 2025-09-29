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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .contact_point_option import ContactPointOption
    from .place import Place
    from .language import Language
    from .opening_hours_specification import OpeningHoursSpecification
    from .administrative_area import AdministrativeArea
    from .geo_shape import GeoShape
    from .product import Product

class ContactPoint(StructuredValue):
    '''
    A contact point&#x2014;for example, a Customer Complaints department.

    Attributes:
        serviceArea: The geographic area where the service is provided.
        email: Email address.
        hoursAvailable: The hours during which this service or contact is available.
        telephone: The telephone number.
        availableLanguage: A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        productSupported: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").
        contactOption: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).
        contactType: A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.
        faxNumber: The fax number.
        areaServed: The geographic area where a service or offered item is provided.
    '''
    class_: Literal['https://schema.org/ContactPoint'] = Field( # type: ignore
        default='https://schema.org/ContactPoint',
        alias='@type',
        serialization_alias='@type'
    )
    serviceArea: Optional[Union['AdministrativeArea', List['AdministrativeArea'], 'GeoShape', List['GeoShape'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceArea',
            'https://schema.org/serviceArea'
        ),
        serialization_alias='https://schema.org/serviceArea'
    )
    email: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'email',
            'https://schema.org/email'
        ),
        serialization_alias='https://schema.org/email'
    )
    hoursAvailable: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hoursAvailable',
            'https://schema.org/hoursAvailable'
        ),
        serialization_alias='https://schema.org/hoursAvailable'
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'telephone',
            'https://schema.org/telephone'
        ),
        serialization_alias='https://schema.org/telephone'
    )
    availableLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
    productSupported: Optional[Union[str, List[str], 'Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productSupported',
            'https://schema.org/productSupported'
        ),
        serialization_alias='https://schema.org/productSupported'
    )
    contactOption: Optional[Union['ContactPointOption', List['ContactPointOption']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactOption',
            'https://schema.org/contactOption'
        ),
        serialization_alias='https://schema.org/contactOption'
    )
    contactType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactType',
            'https://schema.org/contactType'
        ),
        serialization_alias='https://schema.org/contactType'
    )
    faxNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'faxNumber',
            'https://schema.org/faxNumber'
        ),
        serialization_alias='https://schema.org/faxNumber'
    )
    areaServed: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'AdministrativeArea', List['AdministrativeArea'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
