from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .medical_organization import MedicalOrganization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_test import MedicalTest

class DiagnosticLab(MedicalOrganization):
    """
A medical laboratory that offers on-site or off-site diagnostic services.
    """
    class_: Literal['https://schema.org/DiagnosticLab'] = Field( # type: ignore
        default='https://schema.org/DiagnosticLab',
        alias='@type',
        serialization_alias='@type'
    )
    availableTest: Optional[Union["MedicalTest", List["MedicalTest"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableTest',
            'https://schema.org/availableTest'
        ),
        serialization_alias='https://schema.org/availableTest'
    )
