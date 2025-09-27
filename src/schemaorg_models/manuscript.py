from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Manuscript(CreativeWork):
    """
A book, document, or piece of music written by hand rather than typed or printed.
    """
    class_: Literal['https://schema.org/Manuscript'] = Field(default='https://schema.org/Manuscript', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
