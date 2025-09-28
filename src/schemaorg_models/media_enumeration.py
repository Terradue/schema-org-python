from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MediaEnumeration(Enumeration):
    """
MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination.
    """
    class_: Literal['https://schema.org/MediaEnumeration'] = Field( # type: ignore
        default='https://schema.org/MediaEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
