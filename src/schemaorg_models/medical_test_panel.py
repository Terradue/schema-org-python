from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest

from schemaorg_models.medical_test import MedicalTest

class MedicalTestPanel(MedicalTest):
    """
Any collection of tests commonly ordered together.
    """
    subTest: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(default=None,validation_alias=AliasChoices('subTest', 'https://schema.org/subTest'),serialization_alias='https://schema.org/subTest')
