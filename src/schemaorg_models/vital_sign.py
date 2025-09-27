from typing import Literal
from pydantic import Field
from schemaorg_models.medical_sign import MedicalSign


class VitalSign(MedicalSign):
    """
Vital signs are measures of various physiological functions in order to assess the most basic body functions.
    """
    type_: Literal['https://schema.org/VitalSign'] = Field(default='https://schema.org/VitalSign', alias='@type', serialization_alias='@type') # type: ignore
