from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.entertainment_business import EntertainmentBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ArtGallery(EntertainmentBusiness):
    """
An art gallery.
    """
    class_: Literal['https://schema.org/ArtGallery'] = Field( # type: ignore
        default='https://schema.org/ArtGallery',
        alias='@type',
        serialization_alias='@type'
    )
