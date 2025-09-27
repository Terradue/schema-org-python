from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """
A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
    type_: Literal['https://schema.org/PaymentStatusType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PaymentStatusType'),serialization_alias='class') # type: ignore
