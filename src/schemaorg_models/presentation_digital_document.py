from __future__ import annotations

from .digital_document import DigitalDocument    

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
