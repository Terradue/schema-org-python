from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Manuscript(CreativeWork):
    """
A book, document, or piece of music written by hand rather than typed or printed.
    """
    type_: Literal['https://schema.org/Manuscript'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Manuscript'),serialization_alias='class') # type: ignore
