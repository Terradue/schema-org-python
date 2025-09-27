from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    class_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field('class', alias='class', serialization_alias='class') # type: ignore
