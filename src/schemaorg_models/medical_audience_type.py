from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """
Target audiences types for medical web pages. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalAudienceType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalAudienceType'),serialization_alias='class') # type: ignore
