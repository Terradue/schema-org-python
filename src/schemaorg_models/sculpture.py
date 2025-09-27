from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Sculpture(CreativeWork):
    """
A piece of sculpture.
    """
    type_: Literal['https://schema.org/Sculpture'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Sculpture'),serialization_alias='class') # type: ignore
