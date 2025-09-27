from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """
Enumerated status values for Order.
    """
    class_: Literal['https://schema.org/OrderStatus'] = Field('class', alias='class', serialization_alias='class') # type: ignore
