from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.audience import Audience

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalAudience(Audience):
    """
Medical audience for page.
    """
    class_: Literal['https://schema.org/MedicalAudience'] = Field( # type: ignore
        default='https://schema.org/MedicalAudience',
        alias='@type',
        serialization_alias='@type'
    )
