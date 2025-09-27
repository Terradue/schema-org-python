from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """
Enumerated status values for Order.
    """
    type_: Literal['https://schema.org/OrderStatus'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OrderStatus'),serialization_alias='class') # type: ignore
