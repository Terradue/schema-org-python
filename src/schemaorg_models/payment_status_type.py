from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """
A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
    class_: Literal['https://schema.org/PaymentStatusType'] = Field(default='https://schema.org/PaymentStatusType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
