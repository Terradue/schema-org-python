from typing import List, Literal, Optional, Union
from datetime import date
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.web_page_element import WebPageElement
from schemaorg_models.speakable_specification import SpeakableSpecification
from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class WebPage(CreativeWork):
    """
A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.
    """
    class_: Literal['https://schema.org/WebPage'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    mainContentOfPage: Optional[Union[WebPageElement, List[WebPageElement]]] = Field(default=None,validation_alias=AliasChoices('mainContentOfPage', 'https://schema.org/mainContentOfPage'), serialization_alias='https://schema.org/mainContentOfPage')
    significantLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('significantLink', 'https://schema.org/significantLink'), serialization_alias='https://schema.org/significantLink')
    @field_serializer('significantLink')
    def significantLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    speakable: Optional[Union[HttpUrl, List[HttpUrl], SpeakableSpecification, List[SpeakableSpecification]]] = Field(default=None,validation_alias=AliasChoices('speakable', 'https://schema.org/speakable'), serialization_alias='https://schema.org/speakable')
    @field_serializer('speakable')
    def speakable2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    lastReviewed: Optional[Union[date, List[date]]] = Field(default=None,validation_alias=AliasChoices('lastReviewed', 'https://schema.org/lastReviewed'), serialization_alias='https://schema.org/lastReviewed')
    primaryImageOfPage: Optional[Union["ImageObject", List["ImageObject"]]] = Field(default=None,validation_alias=AliasChoices('primaryImageOfPage', 'https://schema.org/primaryImageOfPage'), serialization_alias='https://schema.org/primaryImageOfPage')
    reviewedBy: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('reviewedBy', 'https://schema.org/reviewedBy'), serialization_alias='https://schema.org/reviewedBy')
    relatedLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('relatedLink', 'https://schema.org/relatedLink'), serialization_alias='https://schema.org/relatedLink')
    @field_serializer('relatedLink')
    def relatedLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    significantLinks: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('significantLinks', 'https://schema.org/significantLinks'), serialization_alias='https://schema.org/significantLinks')
    @field_serializer('significantLinks')
    def significantLinks2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    specialty: Optional[Union["Specialty", List["Specialty"]]] = Field(default=None,validation_alias=AliasChoices('specialty', 'https://schema.org/specialty'), serialization_alias='https://schema.org/specialty')
    breadcrumb: Optional[Union[str, List[str], "BreadcrumbList", List["BreadcrumbList"]]] = Field(default=None,validation_alias=AliasChoices('breadcrumb', 'https://schema.org/breadcrumb'), serialization_alias='https://schema.org/breadcrumb')
