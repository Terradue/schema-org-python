from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class _Class(Intangible):
    """
A class, also often called a 'Type'; equivalent to rdfs:Class.
    """
    class_: Literal['https://schema.org/_Class'] = Field(default='https://schema.org/_Class', alias='@type', serialization_alias='@type') # type: ignore
