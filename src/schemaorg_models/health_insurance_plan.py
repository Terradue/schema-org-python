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
    from .health_plan_network import HealthPlanNetwork
    from .contact_point import ContactPoint
    from .health_plan_formulary import HealthPlanFormulary

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    includesHealthPlanNetwork: Optional[Union['HealthPlanNetwork', List['HealthPlanNetwork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    includesHealthPlanFormulary: Optional[Union['HealthPlanFormulary', List['HealthPlanFormulary']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    contactPoint: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanMarketingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    usesHealthPlanIdStandard: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanDrugOption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
