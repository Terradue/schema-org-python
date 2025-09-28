from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_test import MedicalTest

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BloodTest(MedicalTest):
    """
A medical test performed on a sample of a patient's blood.
    """
    class_: Literal['https://schema.org/BloodTest'] = Field( # type: ignore
        default='https://schema.org/BloodTest',
        alias='@type',
        serialization_alias='@type'
    )
