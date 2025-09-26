from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest


class PathologyTest(MedicalTest):
    """
A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.
    """
    tissueSample: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('tissueSample', 'https://schema.org/tissueSample'),serialization_alias='https://schema.org/tissueSample')
