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

class LifestyleModification(MedicalEntity):
    """
A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/LifestyleModification'] = Field( # type: ignore
        default='https://schema.org/LifestyleModification',
        alias='@type',
        serialization_alias='@type'
    )
