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

class PurchaseType(Enumeration):
    """
Optional. The type of purchase the consumer must make in order to qualify for this incentive.
    """
    class_: Literal['https://schema.org/PurchaseType'] = Field( # type: ignore
        default='https://schema.org/PurchaseType',
        alias='@type',
        serialization_alias='@type'
    )
