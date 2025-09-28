from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

from datetime import (
    date
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
from schemaorg_models.web_page_element import WebPageElement
from schemaorg_models.speakable_specification import SpeakableSpecification
from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class WebPage(CreativeWork):
    """
A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.
    """
    class_: Literal['https://schema.org/WebPage'] = Field( # type: ignore
        default='https://schema.org/WebPage',
        alias='@type',
        serialization_alias='@type'
    )
    mainContentOfPage: Optional[Union[WebPageElement, List[WebPageElement]]] = Field(
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
    speakable: Optional[Union[HttpUrl, List[HttpUrl], SpeakableSpecification, List[SpeakableSpecification]]] = Field(
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
    primaryImageOfPage: Optional[Union["ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'primaryImageOfPage',
            'https://schema.org/primaryImageOfPage'
        ),
        serialization_alias='https://schema.org/primaryImageOfPage'
    )
    reviewedBy: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(
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
    specialty: Optional[Union["Specialty", List["Specialty"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'specialty',
            'https://schema.org/specialty'
        ),
        serialization_alias='https://schema.org/specialty'
    )
    breadcrumb: Optional[Union[str, List[str], "BreadcrumbList", List["BreadcrumbList"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'breadcrumb',
            'https://schema.org/breadcrumb'
        ),
        serialization_alias='https://schema.org/breadcrumb'
    )
