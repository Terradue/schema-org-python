from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """
A spreadsheet file.
    """
    class_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field(default='https://schema.org/SpreadsheetDigitalDocument', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
