from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class BookFormatType(Enumeration):
    """
The publication format of the book.
    """
    type_: Literal['https://schema.org/BookFormatType'] = Field(default='https://schema.org/BookFormatType', alias='@type', serialization_alias='@type') # type: ignore
