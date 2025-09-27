from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskCalculator(MedicalRiskEstimator):
    """
A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.
    """
    type_: Literal['https://schema.org/MedicalRiskCalculator'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalRiskCalculator'),serialization_alias='class') # type: ignore
