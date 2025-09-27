from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """
A Buddhist temple.
    """
    class_: Literal['https://schema.org/BuddhistTemple'] = Field(default='https://schema.org/BuddhistTemple', alias='class', serialization_alias='class') # type: ignore
