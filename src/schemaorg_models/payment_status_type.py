from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """
A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
    class_: Literal['https://schema.org/PaymentStatusType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
