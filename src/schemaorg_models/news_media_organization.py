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
from .organization import Organization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .article import Article
    from .about_page import AboutPage
    from .creative_work import CreativeWork

class NewsMediaOrganization(Organization):
    '''
    A News/Media organization such as a newspaper or TV station.

    Attributes:
        ownershipFundingInfo: For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence.   Note that the [[funder]] is also available and can be used to make basic funder information machine-readable.
        actionableFeedbackPolicy: For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.
        noBylinesPolicy: For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement explaining when authors of articles are not named in bylines.
        correctionsPolicy: For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.
        missionCoveragePrioritiesPolicy: For a [[NewsMediaOrganization]], a statement on coverage priorities, including any public agenda or stance on issues.
        verificationFactCheckingPolicy: Disclosure about verification and fact-checking processes for a [[NewsMediaOrganization]] or other fact-checking [[Organization]].
        masthead: For a [[NewsMediaOrganization]], a link to the masthead page or a page listing top editorial management.
        diversityPolicy: Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]. For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.
        unnamedSourcesPolicy: For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about policy on use of unnamed sources and the decision process required.
        diversityStaffingReport: For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.
        ethicsPolicy: Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic and publishing practices, or of a [[Restaurant]], a page describing food source policies. In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.
    '''
    class_: Literal['https://schema.org/NewsMediaOrganization'] = Field( # type: ignore
        default='https://schema.org/NewsMediaOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    ownershipFundingInfo: Optional[Union[str, List[str], 'CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl], 'AboutPage', List['AboutPage']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ownershipFundingInfo',
            'https://schema.org/ownershipFundingInfo'
        ),
        serialization_alias='https://schema.org/ownershipFundingInfo'
    )
    actionableFeedbackPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionableFeedbackPolicy',
            'https://schema.org/actionableFeedbackPolicy'
        ),
        serialization_alias='https://schema.org/actionableFeedbackPolicy'
    )
    noBylinesPolicy: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'noBylinesPolicy',
            'https://schema.org/noBylinesPolicy'
        ),
        serialization_alias='https://schema.org/noBylinesPolicy'
    )
    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'correctionsPolicy',
            'https://schema.org/correctionsPolicy'
        ),
        serialization_alias='https://schema.org/correctionsPolicy'
    )
    missionCoveragePrioritiesPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'missionCoveragePrioritiesPolicy',
            'https://schema.org/missionCoveragePrioritiesPolicy'
        ),
        serialization_alias='https://schema.org/missionCoveragePrioritiesPolicy'
    )
    verificationFactCheckingPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'verificationFactCheckingPolicy',
            'https://schema.org/verificationFactCheckingPolicy'
        ),
        serialization_alias='https://schema.org/verificationFactCheckingPolicy'
    )
    masthead: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'masthead',
            'https://schema.org/masthead'
        ),
        serialization_alias='https://schema.org/masthead'
    )
    diversityPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityPolicy',
            'https://schema.org/diversityPolicy'
        ),
        serialization_alias='https://schema.org/diversityPolicy'
    )
    unnamedSourcesPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unnamedSourcesPolicy',
            'https://schema.org/unnamedSourcesPolicy'
        ),
        serialization_alias='https://schema.org/unnamedSourcesPolicy'
    )
    diversityStaffingReport: Optional[Union['Article', List['Article'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityStaffingReport',
            'https://schema.org/diversityStaffingReport'
        ),
        serialization_alias='https://schema.org/diversityStaffingReport'
    )
    ethicsPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ethicsPolicy',
            'https://schema.org/ethicsPolicy'
        ),
        serialization_alias='https://schema.org/ethicsPolicy'
    )
