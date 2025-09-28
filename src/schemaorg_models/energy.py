from __future__ import annotations

from .quantity import Quantity    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Energy(Quantity):
    """
Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.
    """
    class_: Literal['https://schema.org/Energy'] = Field( # type: ignore
        default='https://schema.org/Energy',
        alias='@type',
        serialization_alias='@type'
    )
