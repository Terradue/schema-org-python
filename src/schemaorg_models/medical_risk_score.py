from __future__ import annotations

from .medical_risk_estimator import MedicalRiskEstimator    

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

class MedicalRiskScore(MedicalRiskEstimator):
    """
A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
    """
    class_: Literal['https://schema.org/MedicalRiskScore'] = Field( # type: ignore
        default='https://schema.org/MedicalRiskScore',
        alias='@type',
        serialization_alias='@type'
    )
    algorithm: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'algorithm',
            'https://schema.org/algorithm'
        ),
        serialization_alias='https://schema.org/algorithm'
    )
