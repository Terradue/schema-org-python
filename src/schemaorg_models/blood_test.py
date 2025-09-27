from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest


class BloodTest(MedicalTest):
    """
A medical test performed on a sample of a patient's blood.
    """
    type_: Literal['https://schema.org/BloodTest'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BloodTest'),serialization_alias='class') # type: ignore
