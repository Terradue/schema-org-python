from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """
A file composed primarily of text.
    """
    class_: Literal['https://schema.org/TextDigitalDocument'] = Field(default='https://schema.org/TextDigitalDocument', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
