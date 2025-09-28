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

class CarUsageType(Enumeration):
    """
A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    """
    class_: Literal['https://schema.org/CarUsageType'] = Field( # type: ignore
        default='https://schema.org/CarUsageType',
        alias='@type',
        serialization_alias='@type'
    )
