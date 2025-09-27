from typing import Literal
from pydantic import Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalContraindication(MedicalEntity):
    """
A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications can be absolute (there are no reasonable circumstances for undertaking a course of action) or relative (the patient is at higher risk of complications, but these risks may be outweighed by other considerations or mitigated by other measures).
    """
    class_: Literal['https://schema.org/MedicalContraindication'] = Field(default='https://schema.org/MedicalContraindication', alias='@type', serialization_alias='@type') # type: ignore
