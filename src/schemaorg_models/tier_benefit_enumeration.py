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

class TierBenefitEnumeration(Enumeration):
    """
An enumeration of possible benefits as part of a loyalty (members) program.
    """
    class_: Literal['https://schema.org/TierBenefitEnumeration'] = Field( # type: ignore
        default='https://schema.org/TierBenefitEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
