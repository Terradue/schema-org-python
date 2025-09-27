from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """
A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
    """
    type_: Literal['https://schema.org/MedicalRiskScore'] = Field(default='https://schema.org/MedicalRiskScore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    algorithm: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('algorithm', 'https://schema.org/algorithm'), serialization_alias='https://schema.org/algorithm')
