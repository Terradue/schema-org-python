from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .lodging_business import LodgingBusiness

class Hostel(LodgingBusiness):
    """
A hostel - cheap accommodation, often in shared dormitories.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/Hostel'] = Field( # type: ignore
        default='https://schema.org/Hostel',
        alias='@type',
        serialization_alias='@type'
    )
