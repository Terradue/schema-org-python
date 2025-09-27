from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class BookFormatType(Enumeration):
    """
The publication format of the book.
    """
    type_: Literal['https://schema.org/BookFormatType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BookFormatType'),serialization_alias='class') # type: ignore
