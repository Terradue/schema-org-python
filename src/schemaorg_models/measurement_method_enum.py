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

class MeasurementMethodEnum(Enumeration):
    """
Enumeration(s) for use with [[measurementMethod]].
    """
    class_: Literal['https://schema.org/MeasurementMethodEnum'] = Field( # type: ignore
        default='https://schema.org/MeasurementMethodEnum',
        alias='@type',
        serialization_alias='@type'
    )
