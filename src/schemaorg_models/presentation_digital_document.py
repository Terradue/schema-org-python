from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.digital_document import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """
A file containing slides or used for a presentation.
    """
    type_: Literal['https://schema.org/PresentationDigitalDocument'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PresentationDigitalDocument'),serialization_alias='class') # type: ignore
