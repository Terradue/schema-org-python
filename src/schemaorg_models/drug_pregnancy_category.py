from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_enumeration import MedicalEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DrugPregnancyCategory(MedicalEnumeration):
    """
Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.
    """
    class_: Literal['https://schema.org/DrugPregnancyCategory'] = Field( # type: ignore
        default='https://schema.org/DrugPregnancyCategory',
        alias='@type',
        serialization_alias='@type'
    )
