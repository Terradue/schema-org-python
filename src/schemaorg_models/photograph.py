from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Photograph(CreativeWork):
    """
A photograph.
    """
    type_: Literal['https://schema.org/Photograph'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Photograph'),serialization_alias='class') # type: ignore
