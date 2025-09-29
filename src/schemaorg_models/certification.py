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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rating import Rating
    from .certification_status_enumeration import CertificationStatusEnumeration
    from .thing import Thing
    from .image_object import ImageObject
    from .administrative_area import AdministrativeArea
    from .defined_term import DefinedTerm
    from .quantitative_value import QuantitativeValue
    from .organization import Organization

class Certification(CreativeWork):
    '''
    A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization. A certification is typically issued by an indendent certification body, for example a professional organization or government. It formally attests certain characteristics about the subject, for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person can be a certified professional, a Place can be certified for food processing. There are certifications for many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc. A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails) class in the GS1 Web Vocabulary.

    Attributes:
        certificationIdentification: Identifier of a certification instance (as registered with an independent certification body). Typically this identifier can be used to consult and verify the certification instance. See also [gs1:certificationIdentification](https://www.gs1.org/voc/certificationIdentification).
        logo: An associated logo.
        about: The subject matter of the content.
        validFrom: The date when the item becomes valid.
        auditDate: Date when a certification was last audited. See also  [gs1:certificationAuditDate](https://www.gs1.org/voc/certificationAuditDate).
        expires: Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited, a [[ClaimReview]] fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a [[Certification]] the validity has expired.
        certificationRating: Rating of a certification instance (as defined by an independent certification body). Typically this rating can be used to rate the level to which the requirements of the certification instance are fulfilled. See also [gs1:certificationValue](https://www.gs1.org/voc/certificationValue).
        validIn: The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]], or an [[EducationalOccupationalCredential]]. 
        hasMeasurement: A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        issuedBy: The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].
        certificationStatus: Indicates the current status of a certification: active or inactive. See also  [gs1:certificationStatus](https://www.gs1.org/voc/certificationStatus).
        datePublished: Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued.
    '''
    class_: Literal['https://schema.org/Certification'] = Field( # type: ignore
        default='https://schema.org/Certification',
        alias='@type',
        serialization_alias='@type'
    )
    certificationIdentification: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    about: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    auditDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expires: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    certificationRating: Optional[Union['Rating', List['Rating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validIn: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasMeasurement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    issuedBy: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    certificationStatus: Optional[Union['CertificationStatusEnumeration', List['CertificationStatusEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    datePublished: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
