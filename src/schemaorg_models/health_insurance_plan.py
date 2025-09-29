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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .contact_point import ContactPoint
    from .health_plan_formulary import HealthPlanFormulary
    from .health_plan_network import HealthPlanNetwork

class HealthInsurancePlan(Intangible):
    '''
    A US-style health insurance plan, including PPOs, EPOs, and HMOs.

    Attributes:
        benefitsSummaryUrl: The URL that goes directly to the summary of benefits and coverage for the specific standard plan or plan variation.
        includesHealthPlanNetwork: Networks covered by this plan.
        includesHealthPlanFormulary: Formularies covered by this plan.
        contactPoint: A contact point for a person or organization.
        healthPlanId: The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across different markets.)
        healthPlanMarketingUrl: The URL that goes directly to the plan brochure for the specific standard plan or plan variation.
        usesHealthPlanIdStandard: The standard for interpreting the Plan ID. The preferred is "HIOS". See the Centers for Medicare & Medicaid Services for more details.
        healthPlanDrugOption: TODO.
        healthPlanDrugTier: The tier(s) of drugs offered by this formulary or insurance plan.
    '''
    class_: Literal['https://schema.org/HealthInsurancePlan'] = Field( # type: ignore
        default='https://schema.org/HealthInsurancePlan',
        alias='@type',
        serialization_alias='@type'
    )
    benefitsSummaryUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'benefitsSummaryUrl',
            'https://schema.org/benefitsSummaryUrl'
        ),
        serialization_alias='https://schema.org/benefitsSummaryUrl'
    )
    includesHealthPlanNetwork: Optional[Union['HealthPlanNetwork', List['HealthPlanNetwork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesHealthPlanNetwork',
            'https://schema.org/includesHealthPlanNetwork'
        ),
        serialization_alias='https://schema.org/includesHealthPlanNetwork'
    )
    includesHealthPlanFormulary: Optional[Union['HealthPlanFormulary', List['HealthPlanFormulary']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesHealthPlanFormulary',
            'https://schema.org/includesHealthPlanFormulary'
        ),
        serialization_alias='https://schema.org/includesHealthPlanFormulary'
    )
    contactPoint: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint',
            'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint'
    )
    healthPlanId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanId',
            'https://schema.org/healthPlanId'
        ),
        serialization_alias='https://schema.org/healthPlanId'
    )
    healthPlanMarketingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanMarketingUrl',
            'https://schema.org/healthPlanMarketingUrl'
        ),
        serialization_alias='https://schema.org/healthPlanMarketingUrl'
    )
    usesHealthPlanIdStandard: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usesHealthPlanIdStandard',
            'https://schema.org/usesHealthPlanIdStandard'
        ),
        serialization_alias='https://schema.org/usesHealthPlanIdStandard'
    )
    healthPlanDrugOption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanDrugOption',
            'https://schema.org/healthPlanDrugOption'
        ),
        serialization_alias='https://schema.org/healthPlanDrugOption'
    )
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanDrugTier',
            'https://schema.org/healthPlanDrugTier'
        ),
        serialization_alias='https://schema.org/healthPlanDrugTier'
    )
