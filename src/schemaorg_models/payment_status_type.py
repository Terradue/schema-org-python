from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """
A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
    type_: Literal['https://schema.org/PaymentStatusType'] = Field(default='https://schema.org/PaymentStatusType', alias='@type', serialization_alias='@type') # type: ignore
