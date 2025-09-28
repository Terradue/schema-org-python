from __future__ import annotations

from .medical_entity import MedicalEntity    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.medical_risk_factor import MedicalRiskFactor

class MedicalRiskEstimator(MedicalEntity):
    """
Any rule set or interactive tool for estimating the risk of developing a complication or condition.
    """
    class_: Literal['https://schema.org/MedicalRiskEstimator'] = Field( # type: ignore
        default='https://schema.org/MedicalRiskEstimator',
        alias='@type',
        serialization_alias='@type'
    )
    estimatesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatesRiskOf',
            'https://schema.org/estimatesRiskOf'
        ),
        serialization_alias='https://schema.org/estimatesRiskOf'
    )
    includedRiskFactor: Optional[Union[MedicalRiskFactor, List[MedicalRiskFactor]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedRiskFactor',
            'https://schema.org/includedRiskFactor'
        ),
        serialization_alias='https://schema.org/includedRiskFactor'
    )
