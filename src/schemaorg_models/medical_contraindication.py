from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_entity import MedicalEntity

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalContraindication(MedicalEntity):
    """
A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications can be absolute (there are no reasonable circumstances for undertaking a course of action) or relative (the patient is at higher risk of complications, but these risks may be outweighed by other considerations or mitigated by other measures).
    """
    class_: Literal['https://schema.org/MedicalContraindication'] = Field( # type: ignore
        default='https://schema.org/MedicalContraindication',
        alias='@type',
        serialization_alias='@type'
    )
