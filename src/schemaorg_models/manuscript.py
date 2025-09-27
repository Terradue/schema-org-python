from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Manuscript(CreativeWork):
    """
A book, document, or piece of music written by hand rather than typed or printed.
    """
    type_: Literal['https://schema.org/Manuscript'] = Field(default='https://schema.org/Manuscript', alias='@type', serialization_alias='@type') # type: ignore
