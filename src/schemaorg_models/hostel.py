from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.lodging_business import LodgingBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

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
