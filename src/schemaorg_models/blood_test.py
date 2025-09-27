from typing import Literal
from pydantic import Field
from schemaorg_models.medical_test import MedicalTest


class BloodTest(MedicalTest):
    """
A medical test performed on a sample of a patient's blood.
    """
    class_: Literal['https://schema.org/BloodTest'] = Field(default='https://schema.org/BloodTest', alias='class', serialization_alias='class') # type: ignore
