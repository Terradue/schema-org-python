from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    type_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field(default='https://schema.org/SpreadsheetDigitalDocument', alias='@type', serialization_alias='@type') # type: ignore
