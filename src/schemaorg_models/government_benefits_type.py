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

class GovernmentBenefitsType(Enumeration):
    """
GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.
    """
    class_: Literal['https://schema.org/GovernmentBenefitsType'] = Field( # type: ignore
        default='https://schema.org/GovernmentBenefitsType',
        alias='@type',
        serialization_alias='@type'
    )
