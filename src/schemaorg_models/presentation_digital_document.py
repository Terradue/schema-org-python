from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .digital_document import DigitalDocument

class PresentationDigitalDocument(DigitalDocument):
    """
A file containing slides or used for a presentation.
    """
    class_: Literal['https://schema.org/PresentationDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/PresentationDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
