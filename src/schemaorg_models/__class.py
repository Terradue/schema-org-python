from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class _Class(Intangible):
    """
A class, also often called a 'Type'; equivalent to rdfs:Class.
    """
    type_: Literal['https://schema.org/_Class'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/_Class'),serialization_alias='class') # type: ignore
