from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """
A file containing slides or used for a presentation.
    """
    type_: Literal['https://schema.org/PresentationDigitalDocument'] = Field(default='https://schema.org/PresentationDigitalDocument', alias='@type', serialization_alias='@type') # type: ignore
