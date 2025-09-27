from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest


class PathologyTest(MedicalTest):
    """
A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.
    """
    class_: Literal['https://schema.org/PathologyTest'] = Field(default='https://schema.org/PathologyTest', alias='class', serialization_alias='class') # type: ignore
    tissueSample: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('tissueSample', 'https://schema.org/tissueSample'), serialization_alias='https://schema.org/tissueSample')
