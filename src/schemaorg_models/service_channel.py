from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.language import Language
from schemaorg_models.service import Service
from schemaorg_models.place import Place

class ServiceChannel(Intangible):
    """
A means for accessing a service, e.g. a government office location, web site, or phone number.
    """
    class_: Literal['https://schema.org/ServiceChannel'] = Field(default='https://schema.org/ServiceChannel', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    processingTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None, validation_alias=AliasChoices('processingTime', 'https://schema.org/processingTime'), serialization_alias='https://schema.org/processingTime')
    availableLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(default=None, validation_alias=AliasChoices('availableLanguage', 'https://schema.org/availableLanguage'), serialization_alias='https://schema.org/availableLanguage')
    servicePostalAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = Field(default=None, validation_alias=AliasChoices('servicePostalAddress', 'https://schema.org/servicePostalAddress'), serialization_alias='https://schema.org/servicePostalAddress')
    providesService: Optional[Union[Service, List[Service]]] = Field(default=None, validation_alias=AliasChoices('providesService', 'https://schema.org/providesService'), serialization_alias='https://schema.org/providesService')
    serviceSmsNumber: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(default=None, validation_alias=AliasChoices('serviceSmsNumber', 'https://schema.org/serviceSmsNumber'), serialization_alias='https://schema.org/serviceSmsNumber')
    serviceUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('serviceUrl', 'https://schema.org/serviceUrl'), serialization_alias='https://schema.org/serviceUrl')
    @field_serializer('serviceUrl')
    def serviceUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    serviceLocation: Optional[Union[Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('serviceLocation', 'https://schema.org/serviceLocation'), serialization_alias='https://schema.org/serviceLocation')
    servicePhone: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(default=None, validation_alias=AliasChoices('servicePhone', 'https://schema.org/servicePhone'), serialization_alias='https://schema.org/servicePhone')
