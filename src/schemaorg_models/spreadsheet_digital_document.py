from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .digital_document import DigitalDocument

class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    class_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/SpreadsheetDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
