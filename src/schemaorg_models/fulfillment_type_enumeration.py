from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class FulfillmentTypeEnumeration(Enumeration):
    """
A type of product fulfillment.
    """
    class_: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/FulfillmentTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
