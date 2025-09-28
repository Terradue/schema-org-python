from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .lodging_business import LodgingBusiness

class Hotel(LodgingBusiness):
    """
A hotel is an establishment that provides lodging paid on a short-term basis (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/Hotel'] = Field( # type: ignore
        default='https://schema.org/Hotel',
        alias='@type',
        serialization_alias='@type'
    )
