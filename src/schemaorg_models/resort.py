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

class Resort(LodgingBusiness):
    """
A resort is a place used for relaxation or recreation, attracting visitors for holidays or vacations. Resorts are places, towns or sometimes commercial establishments operated by a single company (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Resort">http://en.wikipedia.org/wiki/Resort</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    
    """
    class_: Literal['https://schema.org/Resort'] = Field( # type: ignore
        default='https://schema.org/Resort',
        alias='@type',
        serialization_alias='@type'
    )
