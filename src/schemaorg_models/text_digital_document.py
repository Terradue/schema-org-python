from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """
A file composed primarily of text.
    """
    class_: Literal['https://schema.org/TextDigitalDocument'] = Field(default='https://schema.org/TextDigitalDocument', alias='class', serialization_alias='class') # type: ignore
