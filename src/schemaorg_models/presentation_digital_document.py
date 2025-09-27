from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """
A file containing slides or used for a presentation.
    """
    class_: Literal['https://schema.org/PresentationDigitalDocument'] = Field(default='https://schema.org/PresentationDigitalDocument', alias='class', serialization_alias='class') # type: ignore
