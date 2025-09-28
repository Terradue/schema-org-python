from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.qualitative_value import QualitativeValue

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BedType(QualitativeValue):
    """
A type of bed. This is used for indicating the bed or beds available in an accommodation.
    """
    class_: Literal['https://schema.org/BedType'] = Field( # type: ignore
        default='https://schema.org/BedType',
        alias='@type',
        serialization_alias='@type'
    )
