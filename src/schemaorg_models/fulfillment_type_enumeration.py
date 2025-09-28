from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FulfillmentTypeEnumeration(Enumeration):
    """
A type of product fulfillment.
    """
    class_: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/FulfillmentTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
