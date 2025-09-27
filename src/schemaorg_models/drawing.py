from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Drawing(CreativeWork):
    """
A picture or diagram made with a pencil, pen, or crayon rather than paint.
    """
    class_: Literal['https://schema.org/Drawing'] = Field(default='https://schema.org/Drawing', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
