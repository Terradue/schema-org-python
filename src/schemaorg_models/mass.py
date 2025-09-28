from __future__ import annotations

from .quantity import Quantity    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Mass(Quantity):
    """
Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.
    """
    class_: Literal['https://schema.org/Mass'] = Field( # type: ignore
        default='https://schema.org/Mass',
        alias='@type',
        serialization_alias='@type'
    )
