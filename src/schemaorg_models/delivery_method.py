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

class DeliveryMethod(Enumeration):
    """
A sub property of instrument. The method of delivery.
    """
    class_: Literal['https://schema.org/DeliveryMethod'] = Field( # type: ignore
        default='https://schema.org/DeliveryMethod',
        alias='@type',
        serialization_alias='@type'
    )
