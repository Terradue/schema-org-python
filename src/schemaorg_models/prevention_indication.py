from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_indication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """
An indication for preventing an underlying condition, symptom, etc.
    """
    type_: Literal['https://schema.org/PreventionIndication'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PreventionIndication'),serialization_alias='class') # type: ignore
