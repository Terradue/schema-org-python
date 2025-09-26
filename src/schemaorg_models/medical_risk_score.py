from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """
A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
    """
    algorithm: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('algorithm', 'https://schema.org/algorithm'),serialization_alias='https://schema.org/algorithm')
