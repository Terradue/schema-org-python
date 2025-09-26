from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class HealthInsurancePlan(Intangible):
    """
A US-style health insurance plan, including PPOs, EPOs, and HMOs.
    """
    benefitsSummaryUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('benefitsSummaryUrl', 'https://schema.org/benefitsSummaryUrl'),serialization_alias='https://schema.org/benefitsSummaryUrl')
    @field_serializer('benefitsSummaryUrl')
    def benefitsSummaryUrl2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    includesHealthPlanNetwork: Optional[Union["HealthPlanNetwork", List["HealthPlanNetwork"]]] = Field(default=None,validation_alias=AliasChoices('includesHealthPlanNetwork', 'https://schema.org/includesHealthPlanNetwork'),serialization_alias='https://schema.org/includesHealthPlanNetwork')
    includesHealthPlanFormulary: Optional[Union["HealthPlanFormulary", List["HealthPlanFormulary"]]] = Field(default=None,validation_alias=AliasChoices('includesHealthPlanFormulary', 'https://schema.org/includesHealthPlanFormulary'),serialization_alias='https://schema.org/includesHealthPlanFormulary')
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(default=None,validation_alias=AliasChoices('contactPoint', 'https://schema.org/contactPoint'),serialization_alias='https://schema.org/contactPoint')
    healthPlanId: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanId', 'https://schema.org/healthPlanId'),serialization_alias='https://schema.org/healthPlanId')
    healthPlanMarketingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('healthPlanMarketingUrl', 'https://schema.org/healthPlanMarketingUrl'),serialization_alias='https://schema.org/healthPlanMarketingUrl')
    @field_serializer('healthPlanMarketingUrl')
    def healthPlanMarketingUrl2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    usesHealthPlanIdStandard: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('usesHealthPlanIdStandard', 'https://schema.org/usesHealthPlanIdStandard'),serialization_alias='https://schema.org/usesHealthPlanIdStandard')
    @field_serializer('usesHealthPlanIdStandard')
    def usesHealthPlanIdStandard2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    healthPlanDrugOption: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanDrugOption', 'https://schema.org/healthPlanDrugOption'),serialization_alias='https://schema.org/healthPlanDrugOption')
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier'),serialization_alias='https://schema.org/healthPlanDrugTier')
