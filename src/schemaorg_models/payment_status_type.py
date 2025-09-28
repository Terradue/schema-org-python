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

class PaymentStatusType(StatusEnumeration):
    """
A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
    class_: Literal['https://schema.org/PaymentStatusType'] = Field( # type: ignore
        default='https://schema.org/PaymentStatusType',
        alias='@type',
        serialization_alias='@type'
    )
