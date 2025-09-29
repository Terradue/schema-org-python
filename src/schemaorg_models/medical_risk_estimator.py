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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_risk_factor import MedicalRiskFactor

class MedicalRiskEstimator(MedicalEntity):
    '''
    Any rule set or interactive tool for estimating the risk of developing a complication or condition.

    Attributes:
        estimatesRiskOf: The condition, complication, or symptom whose risk is being estimated.
        includedRiskFactor: A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.
    '''
    class_: Literal['https://schema.org/MedicalRiskEstimator'] = Field( # type: ignore
        default='https://schema.org/MedicalRiskEstimator',
        alias='@type',
        serialization_alias='@type'
    )
    estimatesRiskOf: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatesRiskOf',
            'https://schema.org/estimatesRiskOf'
        ),
        serialization_alias='https://schema.org/estimatesRiskOf'
    )
    includedRiskFactor: Optional[Union['MedicalRiskFactor', List['MedicalRiskFactor']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedRiskFactor',
            'https://schema.org/includedRiskFactor'
        ),
        serialization_alias='https://schema.org/includedRiskFactor'
    )
