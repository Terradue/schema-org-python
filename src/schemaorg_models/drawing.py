from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Drawing(CreativeWork):
    """
A picture or diagram made with a pencil, pen, or crayon rather than paint.
    """
    type_: Literal['https://schema.org/Drawing'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Drawing'),serialization_alias='class') # type: ignore
