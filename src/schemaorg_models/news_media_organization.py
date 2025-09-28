from __future__ import annotations
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
from .organization import Organization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .about_page import AboutPage
    from .article import Article
    from .creative_work import CreativeWork

class NewsMediaOrganization(Organization):
    """
A News/Media organization such as a newspaper or TV station.
    """
    class_: Literal['https://schema.org/NewsMediaOrganization'] = Field( # type: ignore
        default='https://schema.org/NewsMediaOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    ownershipFundingInfo: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl], AboutPage, List[AboutPage]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ownershipFundingInfo',
            'https://schema.org/ownershipFundingInfo'
        ),
        serialization_alias='https://schema.org/ownershipFundingInfo'
    )
    actionableFeedbackPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionableFeedbackPolicy',
            'https://schema.org/actionableFeedbackPolicy'
        ),
        serialization_alias='https://schema.org/actionableFeedbackPolicy'
    )
    noBylinesPolicy: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'noBylinesPolicy',
            'https://schema.org/noBylinesPolicy'
        ),
        serialization_alias='https://schema.org/noBylinesPolicy'
    )
    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'correctionsPolicy',
            'https://schema.org/correctionsPolicy'
        ),
        serialization_alias='https://schema.org/correctionsPolicy'
    )
    missionCoveragePrioritiesPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'missionCoveragePrioritiesPolicy',
            'https://schema.org/missionCoveragePrioritiesPolicy'
        ),
        serialization_alias='https://schema.org/missionCoveragePrioritiesPolicy'
    )
    verificationFactCheckingPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'verificationFactCheckingPolicy',
            'https://schema.org/verificationFactCheckingPolicy'
        ),
        serialization_alias='https://schema.org/verificationFactCheckingPolicy'
    )
    masthead: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'masthead',
            'https://schema.org/masthead'
        ),
        serialization_alias='https://schema.org/masthead'
    )
    diversityPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityPolicy',
            'https://schema.org/diversityPolicy'
        ),
        serialization_alias='https://schema.org/diversityPolicy'
    )
    unnamedSourcesPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unnamedSourcesPolicy',
            'https://schema.org/unnamedSourcesPolicy'
        ),
        serialization_alias='https://schema.org/unnamedSourcesPolicy'
    )
    diversityStaffingReport: Optional[Union[Article, List[Article], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityStaffingReport',
            'https://schema.org/diversityStaffingReport'
        ),
        serialization_alias='https://schema.org/diversityStaffingReport'
    )
    ethicsPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ethicsPolicy',
            'https://schema.org/ethicsPolicy'
        ),
        serialization_alias='https://schema.org/ethicsPolicy'
    )
