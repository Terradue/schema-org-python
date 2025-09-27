from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Painting(CreativeWork):
    """
A painting.
    """
    type_: Literal['https://schema.org/Painting'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Painting'),serialization_alias='class') # type: ignore
