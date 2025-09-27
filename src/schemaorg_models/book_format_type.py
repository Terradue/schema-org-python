from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class BookFormatType(Enumeration):
    """
The publication format of the book.
    """
    class_: Literal['https://schema.org/BookFormatType'] = Field(default='https://schema.org/BookFormatType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
