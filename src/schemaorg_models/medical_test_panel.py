from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest

from schemaorg_models.medical_test import MedicalTest

class MedicalTestPanel(MedicalTest):
    """
Any collection of tests commonly ordered together.
    """
    class_: Literal['https://schema.org/MedicalTestPanel'] = Field(default='https://schema.org/MedicalTestPanel', alias='class', serialization_alias='class') # type: ignore
    subTest: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(default=None, validation_alias=AliasChoices('subTest', 'https://schema.org/subTest'), serialization_alias='https://schema.org/subTest')
