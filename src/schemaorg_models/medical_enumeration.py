from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalEnumeration(Enumeration):
    """
Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.
    """
    class_: Literal['https://schema.org/MedicalEnumeration'] = Field( # type: ignore
        default='https://schema.org/MedicalEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
