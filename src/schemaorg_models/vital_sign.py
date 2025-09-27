from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_sign import MedicalSign


class VitalSign(MedicalSign):
    """
Vital signs are measures of various physiological functions in order to assess the most basic body functions.
    """
    type_: Literal['https://schema.org/VitalSign'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VitalSign'),serialization_alias='class') # type: ignore
