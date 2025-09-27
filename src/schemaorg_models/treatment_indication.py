from typing import Literal
from pydantic import Field
from schemaorg_models.medical_indication import MedicalIndication


class TreatmentIndication(MedicalIndication):
    """
An indication for treating an underlying condition, symptom, etc.
    """
    type_: Literal['https://schema.org/TreatmentIndication'] = Field(default='https://schema.org/TreatmentIndication', alias='@type', serialization_alias='@type') # type: ignore
