from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.organization import Organization

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.article import Article

class NewsMediaOrganization(Organization):
    """
A News/Media organization such as a newspaper or TV station.
    """
    ownershipFundingInfo: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl], "AboutPage", List["AboutPage"]]] = Field(default=None,validation_alias=AliasChoices('ownershipFundingInfo', 'https://schema.org/ownershipFundingInfo'),serialization_alias='https://schema.org/ownershipFundingInfo')
    @field_serializer('ownershipFundingInfo')
    def ownershipFundingInfo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    actionableFeedbackPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('actionableFeedbackPolicy', 'https://schema.org/actionableFeedbackPolicy'),serialization_alias='https://schema.org/actionableFeedbackPolicy')
    @field_serializer('actionableFeedbackPolicy')
    def actionableFeedbackPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    noBylinesPolicy: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('noBylinesPolicy', 'https://schema.org/noBylinesPolicy'),serialization_alias='https://schema.org/noBylinesPolicy')
    @field_serializer('noBylinesPolicy')
    def noBylinesPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('correctionsPolicy', 'https://schema.org/correctionsPolicy'),serialization_alias='https://schema.org/correctionsPolicy')
    @field_serializer('correctionsPolicy')
    def correctionsPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    missionCoveragePrioritiesPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('missionCoveragePrioritiesPolicy', 'https://schema.org/missionCoveragePrioritiesPolicy'),serialization_alias='https://schema.org/missionCoveragePrioritiesPolicy')
    @field_serializer('missionCoveragePrioritiesPolicy')
    def missionCoveragePrioritiesPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    verificationFactCheckingPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('verificationFactCheckingPolicy', 'https://schema.org/verificationFactCheckingPolicy'),serialization_alias='https://schema.org/verificationFactCheckingPolicy')
    @field_serializer('verificationFactCheckingPolicy')
    def verificationFactCheckingPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    masthead: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('masthead', 'https://schema.org/masthead'),serialization_alias='https://schema.org/masthead')
    @field_serializer('masthead')
    def masthead2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    diversityPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('diversityPolicy', 'https://schema.org/diversityPolicy'),serialization_alias='https://schema.org/diversityPolicy')
    @field_serializer('diversityPolicy')
    def diversityPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    unnamedSourcesPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('unnamedSourcesPolicy', 'https://schema.org/unnamedSourcesPolicy'),serialization_alias='https://schema.org/unnamedSourcesPolicy')
    @field_serializer('unnamedSourcesPolicy')
    def unnamedSourcesPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    diversityStaffingReport: Optional[Union[Article, List[Article], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('diversityStaffingReport', 'https://schema.org/diversityStaffingReport'),serialization_alias='https://schema.org/diversityStaffingReport')
    @field_serializer('diversityStaffingReport')
    def diversityStaffingReport2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    ethicsPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('ethicsPolicy', 'https://schema.org/ethicsPolicy'),serialization_alias='https://schema.org/ethicsPolicy')
    @field_serializer('ethicsPolicy')
    def ethicsPolicy2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

