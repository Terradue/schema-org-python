from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """
Enumerated status values for Order.
    """
    type_: Literal['https://schema.org/OrderStatus'] = Field(default='https://schema.org/OrderStatus', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
