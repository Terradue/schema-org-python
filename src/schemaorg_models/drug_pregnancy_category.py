from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugPregnancyCategory(MedicalEnumeration):
    """
Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.
    """
    type_: Literal['https://schema.org/DrugPregnancyCategory'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DrugPregnancyCategory'),serialization_alias='class') # type: ignore
