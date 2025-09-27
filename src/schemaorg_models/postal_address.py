from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.contact_point import ContactPoint

from schemaorg_models.country import Country

class PostalAddress(ContactPoint):
    """
The mailing address.
    """
    type_: Literal['https://schema.org/PostalAddress'] = Field(default='https://schema.org/PostalAddress', alias='@type', serialization_alias='@type') # type: ignore
    addressRegion: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('addressRegion', 'https://schema.org/addressRegion'), serialization_alias='https://schema.org/addressRegion')
    postalCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'), serialization_alias='https://schema.org/postalCode')
    streetAddress: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('streetAddress', 'https://schema.org/streetAddress'), serialization_alias='https://schema.org/streetAddress')
    addressCountry: Optional[Union[str, List[str], Country, List[Country]]] = Field(default=None, validation_alias=AliasChoices('addressCountry', 'https://schema.org/addressCountry'), serialization_alias='https://schema.org/addressCountry')
    addressLocality: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('addressLocality', 'https://schema.org/addressLocality'), serialization_alias='https://schema.org/addressLocality')
    extendedAddress: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('extendedAddress', 'https://schema.org/extendedAddress'), serialization_alias='https://schema.org/extendedAddress')
    postOfficeBoxNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('postOfficeBoxNumber', 'https://schema.org/postOfficeBoxNumber'), serialization_alias='https://schema.org/postOfficeBoxNumber')
