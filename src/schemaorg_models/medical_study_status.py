from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """
The status of a medical study. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalStudyStatus'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalStudyStatus'),serialization_alias='class') # type: ignore
