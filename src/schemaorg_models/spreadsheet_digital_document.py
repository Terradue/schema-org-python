from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .digital_document import DigitalDocument

class SpreadsheetDigitalDocument(DigitalDocument):
    '''
    A spreadsheet file.
    '''
    class_: Literal['https://schema.org/SpreadsheetDigitalDocument'] = Field( # type: ignore
        default='https://schema.org/SpreadsheetDigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
