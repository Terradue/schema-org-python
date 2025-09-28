from __future__ import annotations

from .digital_document import DigitalDocument    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    class_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/SpreadsheetDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
