from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class HealthInsurancePlan(Intangible):
    """
A US-style health insurance plan, including PPOs, EPOs, and HMOs.
    """
    type_: Literal['https://schema.org/HealthInsurancePlan'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HealthInsurancePlan'),serialization_alias='class') # type: ignore
    benefitsSummaryUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('benefitsSummaryUrl', 'https://schema.org/benefitsSummaryUrl'),serialization_alias='https://schema.org/benefitsSummaryUrl')
    @field_serializer('benefitsSummaryUrl')
    def benefitsSummaryUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    includesHealthPlanNetwork: Optional[Union["HealthPlanNetwork", List["HealthPlanNetwork"]]] = Field(default=None,validation_alias=AliasChoices('includesHealthPlanNetwork', 'https://schema.org/includesHealthPlanNetwork'),serialization_alias='https://schema.org/includesHealthPlanNetwork')
    includesHealthPlanFormulary: Optional[Union["HealthPlanFormulary", List["HealthPlanFormulary"]]] = Field(default=None,validation_alias=AliasChoices('includesHealthPlanFormulary', 'https://schema.org/includesHealthPlanFormulary'),serialization_alias='https://schema.org/includesHealthPlanFormulary')
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(default=None,validation_alias=AliasChoices('contactPoint', 'https://schema.org/contactPoint'),serialization_alias='https://schema.org/contactPoint')
    healthPlanId: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanId', 'https://schema.org/healthPlanId'),serialization_alias='https://schema.org/healthPlanId')
    healthPlanMarketingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('healthPlanMarketingUrl', 'https://schema.org/healthPlanMarketingUrl'),serialization_alias='https://schema.org/healthPlanMarketingUrl')
    @field_serializer('healthPlanMarketingUrl')
    def healthPlanMarketingUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    usesHealthPlanIdStandard: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('usesHealthPlanIdStandard', 'https://schema.org/usesHealthPlanIdStandard'),serialization_alias='https://schema.org/usesHealthPlanIdStandard')
    @field_serializer('usesHealthPlanIdStandard')
    def usesHealthPlanIdStandard2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    healthPlanDrugOption: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanDrugOption', 'https://schema.org/healthPlanDrugOption'),serialization_alias='https://schema.org/healthPlanDrugOption')
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier'),serialization_alias='https://schema.org/healthPlanDrugTier')
