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
    from .web_page_element import WebPageElement
    from .breadcrumb_list import BreadcrumbList
    from .speakable_specification import SpeakableSpecification
    from .image_object import ImageObject
    from .specialty import Specialty
    from .person import Person
    from .organization import Organization

class WebPage(CreativeWork):
    '''
    A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.

    Attributes:
        mainContentOfPage: Indicates if this web page element is the main subject of the page.
        significantLink: One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.
        speakable: Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.

The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:

1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.

2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.

3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.


For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this
we define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.
         
        lastReviewed: Date on which the content on this web page was last reviewed for accuracy and/or completeness.
        primaryImageOfPage: Indicates the main image on the page.
        reviewedBy: People or organizations that have reviewed the content on this web page for accuracy and/or completeness.
        relatedLink: A link related to this web page, for example to other related web pages.
        significantLinks: The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.
        specialty: One of the domain specialities to which this web page's content applies.
        breadcrumb: A set of links that can help a user understand and navigate a website hierarchy.
    '''
    class_: Literal['https://schema.org/WebPage'] = Field( # type: ignore
        default='https://schema.org/WebPage',
        alias='@type',
        serialization_alias='@type'
    )
    mainContentOfPage: Optional[Union['WebPageElement', List['WebPageElement']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mainContentOfPage',
            'https://schema.org/mainContentOfPage'
        ),
        serialization_alias='https://schema.org/mainContentOfPage'
    )
    significantLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'significantLink',
            'https://schema.org/significantLink'
        ),
        serialization_alias='https://schema.org/significantLink'
    )
    speakable: Optional[Union[HttpUrl, List[HttpUrl], 'SpeakableSpecification', List['SpeakableSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'speakable',
            'https://schema.org/speakable'
        ),
        serialization_alias='https://schema.org/speakable'
    )
    lastReviewed: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lastReviewed',
            'https://schema.org/lastReviewed'
        ),
        serialization_alias='https://schema.org/lastReviewed'
    )
    primaryImageOfPage: Optional[Union['ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'primaryImageOfPage',
            'https://schema.org/primaryImageOfPage'
        ),
        serialization_alias='https://schema.org/primaryImageOfPage'
    )
    reviewedBy: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewedBy',
            'https://schema.org/reviewedBy'
        ),
        serialization_alias='https://schema.org/reviewedBy'
    )
    relatedLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedLink',
            'https://schema.org/relatedLink'
        ),
        serialization_alias='https://schema.org/relatedLink'
    )
    significantLinks: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'significantLinks',
            'https://schema.org/significantLinks'
        ),
        serialization_alias='https://schema.org/significantLinks'
    )
    specialty: Optional[Union['Specialty', List['Specialty']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'specialty',
            'https://schema.org/specialty'
        ),
        serialization_alias='https://schema.org/specialty'
    )
    breadcrumb: Optional[Union[str, List[str], 'BreadcrumbList', List['BreadcrumbList']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'breadcrumb',
            'https://schema.org/breadcrumb'
        ),
        serialization_alias='https://schema.org/breadcrumb'
    )
