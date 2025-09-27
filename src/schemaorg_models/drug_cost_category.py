from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """
Enumerated categories of medical drug costs.
    """
    class_: Literal['https://schema.org/DrugCostCategory'] = Field(default='https://schema.org/DrugCostCategory', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
