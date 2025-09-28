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

class MeasurementTypeEnumeration(Enumeration):
    """
Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.
    """
    class_: Literal['https://schema.org/MeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/MeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
