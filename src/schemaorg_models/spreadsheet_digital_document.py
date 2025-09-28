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

class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    class_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/SpreadsheetDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
