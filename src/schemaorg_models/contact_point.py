from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.structured_value import StructuredValue

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.administrative_area import AdministrativeArea
from schemaorg_models.geo_shape import GeoShape
from schemaorg_models.place import Place
from schemaorg_models.language import Language
from schemaorg_models.product import Product
from schemaorg_models.contact_point_option import ContactPointOption

class ContactPoint(StructuredValue):
    """
A contact point for a person or organization.
    """
    class_: Literal['https://schema.org/ContactPoint'] = Field( # type: ignore
        default='https://schema.org/ContactPoint',
        alias='@type',
        serialization_alias='@type'
    )
    serviceArea: Optional[Union[AdministrativeArea, List[AdministrativeArea], GeoShape, List[GeoShape], Place, List[Place]]] = Field(
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
    hoursAvailable: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(
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
    availableLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
    productSupported: Optional[Union[str, List[str], Product, List[Product]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productSupported',
            'https://schema.org/productSupported'
        ),
        serialization_alias='https://schema.org/productSupported'
    )
    contactOption: Optional[Union[ContactPointOption, List[ContactPointOption]]] = Field(
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
    areaServed: Optional[Union[GeoShape, List[GeoShape], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
