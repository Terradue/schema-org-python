from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_organization import MedicalOrganization

from schemaorg_models.medical_test import MedicalTest

class DiagnosticLab(MedicalOrganization):
    """
A medical laboratory that offers on-site or off-site diagnostic services.
    """
    availableTest: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(default=None,validation_alias=AliasChoices('availableTest', 'https://schema.org/availableTest'),serialization_alias='https://schema.org/availableTest')
