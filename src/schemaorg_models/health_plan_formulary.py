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

class HealthPlanFormulary(Intangible):
    '''
    For a given health insurance plan, the specification for costs and coverage of prescription drugs.

    Attributes:
        offersPrescriptionByMail: Whether prescriptions can be delivered by mail.
        healthPlanDrugTier: The tier(s) of drugs offered by this formulary or insurance plan.
        healthPlanCostSharing: The costs to the patient for services under this network or formulary.
    '''
    class_: Literal['https://schema.org/HealthPlanFormulary'] = Field( # type: ignore
        default='https://schema.org/HealthPlanFormulary',
        alias='@type',
        serialization_alias='@type'
    )
    offersPrescriptionByMail: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offersPrescriptionByMail',
            'https://schema.org/offersPrescriptionByMail'
        ),
        serialization_alias='https://schema.org/offersPrescriptionByMail'
    )
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanDrugTier',
            'https://schema.org/healthPlanDrugTier'
        ),
        serialization_alias='https://schema.org/healthPlanDrugTier'
    )
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCostSharing',
            'https://schema.org/healthPlanCostSharing'
        ),
        serialization_alias='https://schema.org/healthPlanCostSharing'
    )
