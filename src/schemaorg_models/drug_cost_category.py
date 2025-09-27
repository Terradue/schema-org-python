from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """
Enumerated categories of medical drug costs.
    """
    type_: Literal['https://schema.org/DrugCostCategory'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DrugCostCategory'),serialization_alias='class') # type: ignore
