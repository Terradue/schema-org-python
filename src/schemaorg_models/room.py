from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.accommodation import Accommodation

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Room(Accommodation):
    """
A room is a distinguishable space within a structure, usually separated from other spaces by interior walls (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Room">http://en.wikipedia.org/wiki/Room</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/Room'] = Field( # type: ignore
        default='https://schema.org/Room',
        alias='@type',
        serialization_alias='@type'
    )
