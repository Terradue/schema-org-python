from typing import Literal
from pydantic import Field
from schemaorg_models.medical_indication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """
An indication for preventing an underlying condition, symptom, etc.
    """
    type_: Literal['https://schema.org/PreventionIndication'] = Field(default='https://schema.org/PreventionIndication', alias='@type', serialization_alias='@type') # type: ignore
