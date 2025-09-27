from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.digital_document import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    type_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SpreadsheetDigitalDocument'),serialization_alias='class') # type: ignore
