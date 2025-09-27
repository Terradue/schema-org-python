from typing import Literal
from pydantic import Field
from schemaorg_models.medical_indication import MedicalIndication


class TreatmentIndication(MedicalIndication):
    """
An indication for treating an underlying condition, symptom, etc.
    """
    type_: Literal['https://schema.org/TreatmentIndication'] = Field(default='https://schema.org/TreatmentIndication', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
