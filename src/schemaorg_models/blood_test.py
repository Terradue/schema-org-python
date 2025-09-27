from typing import Literal
from pydantic import Field
from schemaorg_models.medical_test import MedicalTest


class BloodTest(MedicalTest):
    """
A medical test performed on a sample of a patient's blood.
    """
    type_: Literal['https://schema.org/BloodTest'] = Field(default='https://schema.org/BloodTest', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
