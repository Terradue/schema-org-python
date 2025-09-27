from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugPregnancyCategory(MedicalEnumeration):
    """
Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.
    """
    class_: Literal['https://schema.org/DrugPregnancyCategory'] = Field(default='https://schema.org/DrugPregnancyCategory', alias='@type', serialization_alias='@type') # type: ignore
