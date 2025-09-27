from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.digital_document import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """
A file composed primarily of text.
    """
    type_: Literal['https://schema.org/TextDigitalDocument'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TextDigitalDocument'),serialization_alias='class') # type: ignore
