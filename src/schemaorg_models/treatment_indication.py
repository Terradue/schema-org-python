from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_indication import MedicalIndication


class TreatmentIndication(MedicalIndication):
    """
An indication for treating an underlying condition, symptom, etc.
    """
    type_: Literal['https://schema.org/TreatmentIndication'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TreatmentIndication'),serialization_alias='class') # type: ignore
