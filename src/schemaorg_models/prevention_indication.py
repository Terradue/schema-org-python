from typing import Literal
from pydantic import Field
from schemaorg_models.medical_indication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """
An indication for preventing an underlying condition, symptom, etc.
    """
    class_: Literal['https://schema.org/PreventionIndication'] = Field('class', alias='class', serialization_alias='class') # type: ignore
