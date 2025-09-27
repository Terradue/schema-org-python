from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """
A Hindu temple.
    """
    class_: Literal['https://schema.org/HinduTemple'] = Field('class', alias='class', serialization_alias='class') # type: ignore
