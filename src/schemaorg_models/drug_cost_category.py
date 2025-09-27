from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """
Enumerated categories of medical drug costs.
    """
    type_: Literal['https://schema.org/DrugCostCategory'] = Field(default='https://schema.org/DrugCostCategory', alias='@type', serialization_alias='@type') # type: ignore
