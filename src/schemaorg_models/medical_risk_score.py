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
from .medical_risk_estimator import MedicalRiskEstimator

class MedicalRiskScore(MedicalRiskEstimator):
    '''
    A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.

    Attributes:
        algorithm: The algorithm or rules to follow to compute the score.
    '''
    class_: Literal['https://schema.org/MedicalRiskScore'] = Field( # type: ignore
        default='https://schema.org/MedicalRiskScore',
        alias='@type',
        serialization_alias='@type'
    )
    algorithm: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
