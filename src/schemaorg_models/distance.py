from __future__ import annotations

from .quantity import Quantity    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Distance(Quantity):
    """
Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.
    """
    class_: Literal['https://schema.org/Distance'] = Field( # type: ignore
        default='https://schema.org/Distance',
        alias='@type',
        serialization_alias='@type'
    )
