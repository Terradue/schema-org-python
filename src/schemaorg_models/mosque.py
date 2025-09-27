from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """
A mosque.
    """
    class_: Literal['https://schema.org/Mosque'] = Field(default='https://schema.org/Mosque', alias='class', serialization_alias='class') # type: ignore
