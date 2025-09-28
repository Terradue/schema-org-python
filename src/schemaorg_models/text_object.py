from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.media_object import MediaObject

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TextObject(MediaObject):
    """
A text file. The text can be unformatted or contain markup, html, etc.
    """
    class_: Literal['https://schema.org/TextObject'] = Field( # type: ignore
        default='https://schema.org/TextObject',
        alias='@type',
        serialization_alias='@type'
    )
