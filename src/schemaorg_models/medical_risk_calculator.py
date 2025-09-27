from typing import Literal
from pydantic import Field
from schemaorg_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskCalculator(MedicalRiskEstimator):
    """
A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.
    """
    class_: Literal['https://schema.org/MedicalRiskCalculator'] = Field(default='https://schema.org/MedicalRiskCalculator', alias='@type', serialization_alias='@type') # type: ignore
