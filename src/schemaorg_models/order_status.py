from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.status_enumeration import StatusEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OrderStatus(StatusEnumeration):
    """
Enumerated status values for Order.
    """
    class_: Literal['https://schema.org/OrderStatus'] = Field( # type: ignore
        default='https://schema.org/OrderStatus',
        alias='@type',
        serialization_alias='@type'
    )
