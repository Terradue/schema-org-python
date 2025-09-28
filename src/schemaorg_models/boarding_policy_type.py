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

class BoardingPolicyType(Enumeration):
    """
A type of boarding policy used by an airline.
    """
    class_: Literal['https://schema.org/BoardingPolicyType'] = Field( # type: ignore
        default='https://schema.org/BoardingPolicyType',
        alias='@type',
        serialization_alias='@type'
    )
