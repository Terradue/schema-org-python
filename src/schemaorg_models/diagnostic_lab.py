from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_organization import MedicalOrganization

from schemaorg_models.medical_test import MedicalTest

class DiagnosticLab(MedicalOrganization):
    """
A medical laboratory that offers on-site or off-site diagnostic services.
    """
    type_: Literal['https://schema.org/DiagnosticLab'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DiagnosticLab'),serialization_alias='class') # type: ignore
    availableTest: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(default=None,validation_alias=AliasChoices('availableTest', 'https://schema.org/availableTest'),serialization_alias='https://schema.org/availableTest')
