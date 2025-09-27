from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Drawing(CreativeWork):
    """
A picture or diagram made with a pencil, pen, or crayon rather than paint.
    """
    class_: Literal['https://schema.org/Drawing'] = Field('class', alias='class', serialization_alias='class') # type: ignore
