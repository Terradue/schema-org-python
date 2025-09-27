from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalDevicePurpose(MedicalEnumeration):
    """
Categories of medical devices, organized by the purpose or intended use of the device.
    """
    type_: Literal['https://schema.org/MedicalDevicePurpose'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalDevicePurpose'),serialization_alias='class') # type: ignore
