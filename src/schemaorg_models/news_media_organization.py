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
    from .about_page import AboutPage
    from .article import Article
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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    actionableFeedbackPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    noBylinesPolicy: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    missionCoveragePrioritiesPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    verificationFactCheckingPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    masthead: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    diversityPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    unnamedSourcesPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    diversityStaffingReport: Optional[Union['Article', List['Article'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    ethicsPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
