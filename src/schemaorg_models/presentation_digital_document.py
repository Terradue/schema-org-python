from typing import Literal
from pydantic import Field
from schemaorg_models.digital_document import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """
A file containing slides or used for a presentation.
    """
    type_: Literal['https://schema.org/PresentationDigitalDocument'] = Field(default='https://schema.org/PresentationDigitalDocument', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
