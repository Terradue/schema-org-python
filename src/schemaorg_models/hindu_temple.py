from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """
A Hindu temple.
    """
    class_: Literal['https://schema.org/HinduTemple'] = Field(default='https://schema.org/HinduTemple', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
