from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """
A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
    """
    type_: Literal['https://schema.org/MedicalRiskScore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalRiskScore'),serialization_alias='class') # type: ignore
    algorithm: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('algorithm', 'https://schema.org/algorithm'),serialization_alias='https://schema.org/algorithm')
