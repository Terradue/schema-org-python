from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class RadioClip(Clip):
    """
A short radio program or a segment/part of a radio program.
    """
    class_: Literal['https://schema.org/RadioClip'] = Field(default='https://schema.org/RadioClip', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
