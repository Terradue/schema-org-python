from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.digital_document import DigitalDocument

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TextDigitalDocument(DigitalDocument):
    """
A file composed primarily of text.
    """
    class_: Literal['https://schema.org/TextDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/TextDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
