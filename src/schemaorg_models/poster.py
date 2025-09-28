from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Poster(CreativeWork):
    """
A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.
    """
    class_: Literal['https://schema.org/Poster'] = Field( # type: ignore
        default='https://schema.org/Poster',
        alias='@type',
        serialization_alias='@type'
    )
