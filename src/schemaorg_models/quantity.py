from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Quantity(Intangible):
    """
Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.
    """
    class_: Literal['https://schema.org/Quantity'] = Field( # type: ignore
        default='https://schema.org/Quantity',
        alias='@type',
        serialization_alias='@type'
    )
