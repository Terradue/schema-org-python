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

class PresentationDigitalDocument(DigitalDocument):
    """
A file containing slides or used for a presentation.
    """
    class_: Literal['https://schema.org/PresentationDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/PresentationDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
