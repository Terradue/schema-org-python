from __future__ import annotations
from datetime import (
    date,
    datetime
)
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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rating import Rating
    from .defined_term import DefinedTerm
    from .organization import Organization
    from .certification_status_enumeration import CertificationStatusEnumeration
    from .thing import Thing
    from .quantitative_value import QuantitativeValue
    from .image_object import ImageObject
    from .administrative_area import AdministrativeArea

class Certification(CreativeWork):
    """
A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization. A certification is typically issued by an indendent certification body, for example a professional organization or government. It formally attests certain characteristics about the subject, for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person can be a certified professional, a Place can be certified for food processing. There are certifications for many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc. A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails) class in the GS1 Web Vocabulary.
    """
    class_: Literal['https://schema.org/Certification'] = Field( # type: ignore
        default='https://schema.org/Certification',
        alias='@type',
        serialization_alias='@type'
    )
    certificationIdentification: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'certificationIdentification',
            'https://schema.org/certificationIdentification'
        ),
        serialization_alias='https://schema.org/certificationIdentification'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    about: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'about',
            'https://schema.org/about'
        ),
        serialization_alias='https://schema.org/about'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFrom',
            'https://schema.org/validFrom'
        ),
        serialization_alias='https://schema.org/validFrom'
    )
    auditDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'auditDate',
            'https://schema.org/auditDate'
        ),
        serialization_alias='https://schema.org/auditDate'
    )
    expires: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expires',
            'https://schema.org/expires'
        ),
        serialization_alias='https://schema.org/expires'
    )
    certificationRating: Optional[Union["Rating", List["Rating"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'certificationRating',
            'https://schema.org/certificationRating'
        ),
        serialization_alias='https://schema.org/certificationRating'
    )
    validIn: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validIn',
            'https://schema.org/validIn'
        ),
        serialization_alias='https://schema.org/validIn'
    )
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement',
            'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement'
    )
    issuedBy: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issuedBy',
            'https://schema.org/issuedBy'
        ),
        serialization_alias='https://schema.org/issuedBy'
    )
    certificationStatus: Optional[Union["CertificationStatusEnumeration", List["CertificationStatusEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'certificationStatus',
            'https://schema.org/certificationStatus'
        ),
        serialization_alias='https://schema.org/certificationStatus'
    )
    datePublished: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePublished',
            'https://schema.org/datePublished'
        ),
        serialization_alias='https://schema.org/datePublished'
    )
