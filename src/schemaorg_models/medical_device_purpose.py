from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalDevicePurpose(MedicalEnumeration):
    """
Categories of medical devices, organized by the purpose or intended use of the device.
    """
    class_: Literal['https://schema.org/MedicalDevicePurpose'] = Field('class', alias='class', serialization_alias='class') # type: ignore
