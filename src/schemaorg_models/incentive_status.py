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

class IncentiveStatus(Enumeration):
    """
Enumerates a status for an incentive, such as whether it is active.
    """
    class_: Literal['https://schema.org/IncentiveStatus'] = Field( # type: ignore
        default='https://schema.org/IncentiveStatus',
        alias='@type',
        serialization_alias='@type'
    )
